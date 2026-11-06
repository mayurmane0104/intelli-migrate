# mailbox — Manipulate mailboxes in various formats — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/mailbox.html](https://docs.python.org/3.13/library/mailbox.html)

---

`mailbox` — Manipulate mailboxes in various formats[¶](#module-mailbox)

**Source code:** [Lib/mailbox.py](https://github.com/python/cpython/tree/3.13/Lib/mailbox.py)

This module defines two classes, [ Mailbox](#mailbox.Mailbox) and 

[, for accessing and manipulating on-disk mailboxes and the messages they contain.](#mailbox.Message)

`Message``Mailbox` offers a dictionary-like mapping from keys to messages.
`Message` extends the [module’s](email.message.html#module-email.message)

`email.message`[class with format-specific state and behavior. Supported mailbox formats are Maildir, mbox, MH, Babyl, and MMDF.](email.compat32-message.html#email.message.Message)

`Message`See also

- Module `email`
- Represent and manipulate messages. 

`Mailbox` objects[¶](#mailbox-objects)

- 
*class*mailbox.Mailbox[¶](#mailbox.Mailbox)
- A mailbox, which may be inspected and modified. - The - `Mailbox`class defines an interface and is not intended to be instantiated. Instead, format-specific subclasses should inherit from- `Mailbox`and your code should instantiate a particular subclass.- The - `Mailbox`interface is dictionary-like, with small keys corresponding to messages. Keys are issued by the- `Mailbox`instance with which they will be used and are only meaningful to that- `Mailbox`instance. A key continues to identify a message even if the corresponding message is modified, such as by replacing it with another message.- Messages may be added to a - `Mailbox`instance using the set-like method- `add()`- `del`statement or the set-like methods- `remove()`- `discard()`- `Mailbox`interface semantics differ from dictionary semantics in some noteworthy ways. Each time a message is requested, a new representation (typically a- `Message`- `Mailbox`instance, the provided message representation’s contents are copied. In neither case is a reference to the message representation kept by the- `Mailbox`instance.- The default - `Mailbox`- [iterator](../glossary.html#term-iterator)iterates over message representations, not keys as the default- `dictionary`- `KeyError`- Warning - Be very cautious when modifying mailboxes that might be simultaneously changed by some other process. The safest mailbox format to use for such tasks is - `Maildir`- `mbox`- *must*lock it by calling the- `lock()`- `unlock()`- *before*reading any messages in the file or making any changes by adding or deleting a message. Failing to lock the mailbox runs the risk of losing messages or corrupting the entire mailbox.- `Mailbox`instances have the following methods:- 
add(*message*)[¶](#mailbox.Mailbox.add)
- Add - *message*to the mailbox and return the key that has been assigned to it.- Parameter - *message*may be a- `Message`- `email.message.Message`- *message*is an instance of the appropriate format-specific- `Message`subclass (e.g., if it’s an- `mboxMessage`- `mbox`- Changed in version 3.2: Support for binary input was added. 
 - 
remove(*key*)[¶](#mailbox.Mailbox.remove)
- 
__delitem__(*key*)[¶](#mailbox.Mailbox.__delitem__)
- 
discard(*key*)[¶](#mailbox.Mailbox.discard)
- Delete the message corresponding to - *key*from the mailbox.- If no such message exists, a - `KeyError`- `remove()`or- `__delitem__()`but no exception is raised if the method was called as- `discard()`. The behavior of- `discard()`may be preferred if the underlying mailbox format supports concurrent modification by other processes.
 - 
__setitem__(*key*,*message*)[¶](#mailbox.Mailbox.__setitem__)
- Replace the message corresponding to - *key*with- *message*. Raise a- `KeyError`- *key*.- As with - `add()`- *message*may be a- `Message`- `email.message.Message`- *message*is an instance of the appropriate format-specific- `Message`subclass (e.g., if it’s an- `mboxMessage`- `mbox`- *key*is left unchanged.
 - 
keys()[¶](#mailbox.Mailbox.keys)
- The same as - `iterkeys()`- `list`- [iterator](../glossary.html#term-iterator)
 - 
itervalues()[¶](#mailbox.Mailbox.itervalues)
- 
__iter__()[¶](#mailbox.Mailbox.__iter__)
- Return an - [iterator](../glossary.html#term-iterator)over representations of all messages. The messages are represented as instances of the appropriate format-specific- `Message`- `Mailbox`instance was initialized.- Note - The behavior of - `__iter__()`is unlike that of dictionaries, which iterate over keys.
 - 
values()[¶](#mailbox.Mailbox.values)
- The same as - `itervalues()`- `list`- [iterator](../glossary.html#term-iterator)
 - 
iteritems()[¶](#mailbox.Mailbox.iteritems)
- Return an - [iterator](../glossary.html#term-iterator)over (- *key*,- *message*) pairs, where- *key*is a key and- *message*is a message representation. The messages are represented as instances of the appropriate format-specific- `Message`- `Mailbox`instance was initialized.
 - 
items()[¶](#mailbox.Mailbox.items)
- The same as - `iteritems()`- `list`- [iterator](../glossary.html#term-iterator)of pairs.
 - 
get(*key*,*default=None*)[¶](#mailbox.Mailbox.get)
- 
__getitem__(*key*)[¶](#mailbox.Mailbox.__getitem__)
- Return a representation of the message corresponding to - *key*. If no such message exists,- *default*is returned if the method was called as- `get()`and a- `KeyError`- `__getitem__()`. The message is represented as an instance of the appropriate format-specific- `Message`- `Mailbox`instance was initialized.
 - 
get_message(*key*)[¶](#mailbox.Mailbox.get_message)
- Return a representation of the message corresponding to - *key*as an instance of the appropriate format-specific- `Message`- `KeyError`
 - 
get_bytes(*key*)[¶](#mailbox.Mailbox.get_bytes)
- Return a byte representation of the message corresponding to - *key*, or raise a- `KeyError`- Added in version 3.2. 
 - 
get_string(*key*)[¶](#mailbox.Mailbox.get_string)
- Return a string representation of the message corresponding to - *key*, or raise a- `KeyError`- `email.message.Message`
 - 
get_file(*key*)[¶](#mailbox.Mailbox.get_file)
- Return a - [file-like](../glossary.html#term-file-like-object)representation of the message corresponding to- *key*, or raise a- `KeyError`- Changed in version 3.2: The file object really is a - [binary file](../glossary.html#term-binary-file); previously it was incorrectly returned in text mode. Also, the- [file-like object](../glossary.html#term-file-like-object)now supports the- [context manager](../glossary.html#term-context-manager)protocol: you can use a- `with`- Note - Unlike other representations of messages, - [file-like](../glossary.html#term-file-like-object)representations are not necessarily independent of the- `Mailbox`instance that created them or of the underlying mailbox. More specific documentation is provided by each subclass.
 - 
__contains__(*key*)[¶](#mailbox.Mailbox.__contains__)
- Return - `True`if- *key*corresponds to a message,- `False`otherwise.
 - 
__len__()[¶](#mailbox.Mailbox.__len__)
- Return a count of messages in the mailbox. 
 - 
clear()[¶](#mailbox.Mailbox.clear)
- Delete all messages from the mailbox. 
 - 
pop(*key*,*default=None*)[¶](#mailbox.Mailbox.pop)
- Return a representation of the message corresponding to - *key*and delete the message. If no such message exists, return- *default*. The message is represented as an instance of the appropriate format-specific- `Message`- `Mailbox`instance was initialized.
 - 
popitem()[¶](#mailbox.Mailbox.popitem)
- Return an arbitrary ( - *key*,- *message*) pair, where- *key*is a key and- *message*is a message representation, and delete the corresponding message. If the mailbox is empty, raise a- `KeyError`- `Message`- `Mailbox`instance was initialized.
 - 
update(*arg*)[¶](#mailbox.Mailbox.update)
- Parameter - *arg*should be a- *key*-to-- *message*mapping or an iterable of (- *key*,- *message*) pairs. Updates the mailbox so that, for each given- *key*and- *message*, the message corresponding to- *key*is set to- *message*as if by using- `__setitem__()`- `__setitem__()`, each- *key*must already correspond to a message in the mailbox or else a- `KeyError`- *arg*to be a- `Mailbox`instance.- Note - Unlike with dictionaries, keyword arguments are not supported. 
 - 
flush()[¶](#mailbox.Mailbox.flush)
- Write any pending changes to the filesystem. For some - `Mailbox`subclasses, changes are always written immediately and- `flush()`does nothing, but you should still make a habit of calling this method.
 - 
lock()[¶](#mailbox.Mailbox.lock)
- Acquire an exclusive advisory lock on the mailbox so that other processes know not to modify it. An - `ExternalClashError`- *always*lock the mailbox before making any modifications to its contents.
 - 
unlock()[¶](#mailbox.Mailbox.unlock)
- Release the lock on the mailbox, if any. 
 - 
close()[¶](#mailbox.Mailbox.close)
- Flush the mailbox, unlock it if necessary, and close any open files. For some - `Mailbox`subclasses, this method does nothing.
 
- 
add(

`Maildir` objects[¶](#maildir-objects)

- 
*class*mailbox.Maildir(*dirname*,*factory=None*,*create=True*)[¶](#mailbox.Maildir)
- A subclass of - `Mailbox`- *factory*is a callable object that accepts a file-like message representation (which behaves as if opened in binary mode) and returns a custom representation. If- *factory*is- `None`,- `MaildirMessage`- *create*is- `True`, the mailbox is created if it does not exist.- If - *create*is- `True`and the- *dirname*path exists, it will be treated as an existing maildir without attempting to verify its directory layout.- It is for historical reasons that - *dirname*is named as such rather than- *path*.- Maildir is a directory-based mailbox format invented for the qmail mail transfer agent and now widely supported by other programs. Messages in a Maildir mailbox are stored in separate files within a common directory structure. This design allows Maildir mailboxes to be accessed and modified by multiple unrelated programs without data corruption, so file locking is unnecessary. - Maildir mailboxes contain three subdirectories, namely: - `tmp`,- `new`, and- `cur`. Messages are created momentarily in the- `tmp`subdirectory and then moved to the- `new`subdirectory to finalize delivery. A mail user agent may subsequently move the message to the- `cur`subdirectory and store information about the state of the message in a special “info” section appended to its file name.- Folders of the style introduced by the Courier mail transfer agent are also supported. Any subdirectory of the main mailbox is considered a folder if - `'.'`is the first character in its name. Folder names are represented by- `Maildir`without the leading- `'.'`. Each folder is itself a Maildir mailbox but should not contain other folders. Instead, a logical nesting is indicated using- `'.'`to delimit levels, e.g., “Archived.2005.07”.- 
colon[¶](#mailbox.Maildir.colon)
- The Maildir specification requires the use of a colon ( - `':'`) in certain message file names. However, some operating systems do not permit this character in file names, If you wish to use a Maildir-like format on such an operating system, you should specify another character to use instead. The exclamation point (- `'!'`) is a popular choice. For example:- import mailbox mailbox.Maildir.colon = '!' - The - `colon`attribute may also be set on a per-instance basis.
 - Changed in version 3.13: - `Maildir`now ignores files with a leading dot.- `Maildir`instances have all of the methods of- `Mailbox`- 
list_folders()[¶](#mailbox.Maildir.list_folders)
- Return a list of the names of all folders. 
 - 
get_folder(*folder*)[¶](#mailbox.Maildir.get_folder)
- Return a - `Maildir`instance representing the folder whose name is- *folder*. A- `NoSuchMailboxError`
 - 
add_folder(*folder*)[¶](#mailbox.Maildir.add_folder)
- Create a folder whose name is - *folder*and return a- `Maildir`instance representing it.
 - 
remove_folder(*folder*)[¶](#mailbox.Maildir.remove_folder)
- Delete the folder whose name is - *folder*. If the folder contains any messages, a- `NotEmptyError`
 - 
clean()[¶](#mailbox.Maildir.clean)
- Delete temporary files from the mailbox that have not been accessed in the last 36 hours. The Maildir specification says that mail-reading programs should do this occasionally. 
 - 
get_flags(*key*)[¶](#mailbox.Maildir.get_flags)
- Return as a string the flags that are set on the message corresponding to - *key*. This is the same as- `get_message(key).get_flags()`but much faster, because it does not open the message file. Use this method when iterating over the keys to determine which messages are interesting to get.- If you do have a - `MaildirMessage`- `get_flags()`- `set_flags()`- `add_flag()`- `remove_flag()`- `__setitem__()`- Added in version 3.13. 
 - 
set_flags(*key*,*flags*)[¶](#mailbox.Maildir.set_flags)
- On the message corresponding to - *key*, set the flags specified by- *flags*and unset all others. Calling- `some_mailbox.set_flags(key, flags)`is similar to- one_message = some_mailbox.get_message(key) one_message.set_flags(flags) some_mailbox[key] = one_message - but faster, because it does not open the message file. - If you do have a - `MaildirMessage`- `set_flags()`- `get_flags()`- Added in version 3.13. 
 - 
add_flag(*key*,*flag*)[¶](#mailbox.Maildir.add_flag)
- On the message corresponding to - *key*, set the flags specified by- *flag*without changing other flags. To add more than one flag at a time,- *flag*may be a string of more than one character.- Considerations for using this method versus the message object’s - `add_flag()`- `set_flags()`- Added in version 3.13. 
 - 
remove_flag(*key*,*flag*)[¶](#mailbox.Maildir.remove_flag)
- On the message corresponding to - *key*, unset the flags specified by- *flag*without changing other flags. To remove more than one flag at a time,- *flag*may be a string of more than one character.- Considerations for using this method versus the message object’s - `remove_flag()`- `set_flags()`- Added in version 3.13. 
 - 
get_info(*key*)[¶](#mailbox.Maildir.get_info)
- Return a string containing the info for the message corresponding to - *key*. This is the same as- `get_message(key).get_info()`but much faster, because it does not open the message file. Use this method when iterating over the keys to determine which messages are interesting to get.- If you do have a - `MaildirMessage`- `get_info()`- `set_info()`- `__setitem__()`- Added in version 3.13. 
 - 
set_info(*key*,*info*)[¶](#mailbox.Maildir.set_info)
- Set the info of the message corresponding to - *key*to- *info*. Calling- `some_mailbox.set_info(key, flags)`is similar to- one_message = some_mailbox.get_message(key) one_message.set_info(info) some_mailbox[key] = one_message - but faster, because it does not open the message file. - If you do have a - `MaildirMessage`- `set_info()`- `get_info()`- Added in version 3.13. 
 - Some - `Mailbox`- `Maildir`deserve special remarks:- 
add(*message*)[¶](#mailbox.Maildir.add)
- 
__setitem__(*key*,*message*)[¶](#mailbox.Maildir.__setitem__)
- 
update(*arg*)[¶](#mailbox.Maildir.update)
- Warning - These methods generate unique file names based upon the current process ID. When using multiple threads, undetected name clashes may occur and cause corruption of the mailbox unless threads are coordinated to avoid using these methods to manipulate the same mailbox simultaneously. 
 - 
flush()[¶](#mailbox.Maildir.flush)
- All changes to Maildir mailboxes are immediately applied, so this method does nothing. 
 - 
lock()[¶](#mailbox.Maildir.lock)
- 
unlock()[¶](#mailbox.Maildir.unlock)
- Maildir mailboxes do not support (or require) locking, so these methods do nothing. 
 - 
close()[¶](#mailbox.Maildir.close)
- `Maildir`instances do not keep any open files and the underlying mailboxes do not support locking, so this method does nothing.
 - 
get_file(*key*)[¶](#mailbox.Maildir.get_file)
- Depending upon the host platform, it may not be possible to modify or remove the underlying message while the returned file remains open. 
 
- 
colon

See also

- [maildir man page from Courier](https://www.courier-mta.org/maildir.html)
- A specification of the format. Describes a common extension for supporting folders. 
- [Using maildir format](https://cr.yp.to/proto/maildir.html)
- Notes on Maildir by its inventor. Includes an updated name-creation scheme and details on “info” semantics. 

`mbox` objects[¶](#mbox-objects)

- 
*class*mailbox.mbox(*path*,*factory=None*,*create=True*)[¶](#mailbox.mbox)
- A subclass of - `Mailbox`- *factory*is a callable object that accepts a file-like message representation (which behaves as if opened in binary mode) and returns a custom representation. If- *factory*is- `None`,- `mboxMessage`- *create*is- `True`, the mailbox is created if it does not exist.- The mbox format is the classic format for storing mail on Unix systems. All messages in an mbox mailbox are stored in a single file with the beginning of each message indicated by a line whose first five characters are “From “. - Several variations of the mbox format exist to address perceived shortcomings in the original. In the interest of compatibility, - `mbox`implements the original format, which is sometimes referred to as- *mboxo*. This means that the- *Content-Length*header, if present, is ignored and that any occurrences of “From “ at the beginning of a line in a message body are transformed to “>From “ when storing the message, although occurrences of “>From “ are not transformed to “From “ when reading the message.- Some - `Mailbox`- `mbox`deserve special remarks:- 
get_bytes(*key*,*from_=False*)[¶](#mailbox.mbox.get_bytes)
- Note: This method has an extra parameter ( - *from_*) compared with other classes. The first line of an mbox file entry is the Unix “From “ line. If- *from_*is False, the first line of the file is dropped.
 - 
get_file(*key*,*from_=False*)[¶](#mailbox.mbox.get_file)
- Using the file after calling - `flush()`- `close()`- `mbox`instance may yield unpredictable results or raise an exception.- Note: This method has an extra parameter ( - *from_*) compared with other classes. The first line of an mbox file entry is the Unix “From “ line. If- *from_*is False, the first line of the file is dropped.
 - 
get_string(*key*,*from_=False*)[¶](#mailbox.mbox.get_string)
- Note: This method has an extra parameter ( - *from_*) compared with other classes. The first line of an mbox file entry is the Unix “From “ line. If- *from_*is False, the first line of the file is dropped.
 
- 
get_bytes(

See also

- [mbox man page from tin](http://www.tin.org/bin/man.cgi?section=5&topic=mbox)
- A specification of the format, with details on locking. 
- [Configuring Netscape Mail on Unix: Why The Content-Length Format is Bad](https://www.jwz.org/doc/content-length.html)
- An argument for using the original mbox format rather than a variation. 
- [“mbox” is a family of several mutually incompatible mailbox formats](https://www.loc.gov/preservation/digital/formats/fdd/fdd000383.shtml)
- A history of mbox variations. 

`MH` objects[¶](#mh-objects)

- 
*class*mailbox.MH(*path*,*factory=None*,*create=True*)[¶](#mailbox.MH)
- A subclass of - `Mailbox`- *factory*is a callable object that accepts a file-like message representation (which behaves as if opened in binary mode) and returns a custom representation. If- *factory*is- `None`,- `MHMessage`- *create*is- `True`, the mailbox is created if it does not exist.- MH is a directory-based mailbox format invented for the MH Message Handling System, a mail user agent. Each message in an MH mailbox resides in its own file. An MH mailbox may contain other MH mailboxes (called - *folders*) in addition to messages. Folders may be nested indefinitely. MH mailboxes also support- *sequences*, which are named lists used to logically group messages without moving them to sub-folders. Sequences are defined in a file called- `.mh_sequences`in each folder.- The - `MH`class manipulates MH mailboxes, but it does not attempt to emulate all of- **mh**’s behaviors. In particular, it does not modify and is not affected by the- `context`or- `.mh_profile`files that are used by- **mh**to store its state and configuration.- `MH`instances have all of the methods of- `Mailbox`- Changed in version 3.13: Supported folders that don’t contain a - `.mh_sequences`file.- 
list_folders()[¶](#mailbox.MH.list_folders)
- Return a list of the names of all folders. 
 - 
get_folder(*folder*)[¶](#mailbox.MH.get_folder)
- Return an - `MH`instance representing the folder whose name is- *folder*. A- `NoSuchMailboxError`
 - 
add_folder(*folder*)[¶](#mailbox.MH.add_folder)
- Create a folder whose name is - *folder*and return an- `MH`instance representing it.
 - 
remove_folder(*folder*)[¶](#mailbox.MH.remove_folder)
- Delete the folder whose name is - *folder*. If the folder contains any messages, a- `NotEmptyError`
 - 
get_sequences()[¶](#mailbox.MH.get_sequences)
- Return a dictionary of sequence names mapped to key lists. If there are no sequences, the empty dictionary is returned. 
 - 
set_sequences(*sequences*)[¶](#mailbox.MH.set_sequences)
- Re-define the sequences that exist in the mailbox based upon - *sequences*, a dictionary of names mapped to key lists, like returned by- `get_sequences()`
 - 
pack()[¶](#mailbox.MH.pack)
- Rename messages in the mailbox as necessary to eliminate gaps in numbering. Entries in the sequences list are updated correspondingly. - Note - Already-issued keys are invalidated by this operation and should not be subsequently used. 
 - Some - `Mailbox`- `MH`deserve special remarks:- 
remove(*key*)[¶](#mailbox.MH.remove)
- 
__delitem__(*key*)[¶](#mailbox.MH.__delitem__)
- 
discard(*key*)[¶](#mailbox.MH.discard)
- These methods immediately delete the message. The MH convention of marking a message for deletion by prepending a comma to its name is not used. 
 - 
lock()[¶](#mailbox.MH.lock)
- 
unlock()[¶](#mailbox.MH.unlock)
- Three locking mechanisms are used—dot locking and, if available, the - `flock()`and- `lockf()`system calls. For MH mailboxes, locking the mailbox means locking the- `.mh_sequences`file and, only for the duration of any operations that affect them, locking individual message files.
 - 
get_file(*key*)[¶](#mailbox.MH.get_file)
- Depending upon the host platform, it may not be possible to remove the underlying message while the returned file remains open. 
 - 
flush()[¶](#mailbox.MH.flush)
- All changes to MH mailboxes are immediately applied, so this method does nothing. 
 
- 
list_folders()

See also

- [nmh - Message Handling System](https://www.nongnu.org/nmh/)
- Home page of - **nmh**, an updated version of the original- **mh**.
- [MH & nmh: Email for Users & Programmers](https://rand-mh.sourceforge.io/book/)
- A GPL-licensed book on - **mh**and- **nmh**, with some information on the mailbox format.

`Babyl` objects[¶](#babyl-objects)

- 
*class*mailbox.Babyl(*path*,*factory=None*,*create=True*)[¶](#mailbox.Babyl)
- A subclass of - `Mailbox`- *factory*is a callable object that accepts a file-like message representation (which behaves as if opened in binary mode) and returns a custom representation. If- *factory*is- `None`,- `BabylMessage`- *create*is- `True`, the mailbox is created if it does not exist.- Babyl is a single-file mailbox format used by the Rmail mail user agent included with Emacs. The beginning of a message is indicated by a line containing the two characters Control-Underscore ( - `'\037'`) and Control-L (- `'\014'`). The end of a message is indicated by the start of the next message or, in the case of the last message, a line containing a Control-Underscore (- `'\037'`) character.- Messages in a Babyl mailbox have two sets of headers, original headers and so-called visible headers. Visible headers are typically a subset of the original headers that have been reformatted or abridged to be more attractive. Each message in a Babyl mailbox also has an accompanying list of - *labels*, or short strings that record extra information about the message, and a list of all user-defined labels found in the mailbox is kept in the Babyl options section.- `Babyl`instances have all of the methods of- `Mailbox`- 
get_labels()[¶](#mailbox.Babyl.get_labels)
- Return a list of the names of all user-defined labels used in the mailbox. - Note - The actual messages are inspected to determine which labels exist in the mailbox rather than consulting the list of labels in the Babyl options section, but the Babyl section is updated whenever the mailbox is modified. 
 - Some - `Mailbox`- `Babyl`deserve special remarks:- 
get_file(*key*)[¶](#mailbox.Babyl.get_file)
- In Babyl mailboxes, the headers of a message are not stored contiguously with the body of the message. To generate a file-like representation, the headers and body are copied together into an - `io.BytesIO`
 
- 
get_labels()

See also

- [Format of Version 5 Babyl Files](https://quimby.gnus.org/notes/BABYL)
- A specification of the Babyl format. 
- [Reading Mail with Rmail](https://www.gnu.org/software/emacs/manual/html_node/emacs/Rmail.html)
- The Rmail manual, with some information on Babyl semantics. 

`MMDF` objects[¶](#mmdf-objects)

- 
*class*mailbox.MMDF(*path*,*factory=None*,*create=True*)[¶](#mailbox.MMDF)
- A subclass of - `Mailbox`- *factory*is a callable object that accepts a file-like message representation (which behaves as if opened in binary mode) and returns a custom representation. If- *factory*is- `None`,- `MMDFMessage`- *create*is- `True`, the mailbox is created if it does not exist.- MMDF is a single-file mailbox format invented for the Multichannel Memorandum Distribution Facility, a mail transfer agent. Each message is in the same form as an mbox message but is bracketed before and after by lines containing four Control-A ( - `'\001'`) characters. As with the mbox format, the beginning of each message is indicated by a line whose first five characters are “From “, but additional occurrences of “From “ are not transformed to “>From “ when storing messages because the extra message separator lines prevent mistaking such occurrences for the starts of subsequent messages.- Some - `Mailbox`- `MMDF`deserve special remarks:- 
get_bytes(*key*,*from_=False*)[¶](#mailbox.MMDF.get_bytes)
- Note: This method has an extra parameter ( - *from_*) compared with other classes. The first line of an mbox file entry is the Unix “From “ line. If- *from_*is False, the first line of the file is dropped.
 - 
get_file(*key*,*from_=False*)[¶](#mailbox.MMDF.get_file)
- Using the file after calling - `flush()`- `close()`- `MMDF`instance may yield unpredictable results or raise an exception.- Note: This method has an extra parameter ( - *from_*) compared with other classes. The first line of an mbox file entry is the Unix “From “ line. If- *from_*is False, the first line of the file is dropped.
 
- 
get_bytes(

See also

- [mmdf man page from tin](http://www.tin.org/bin/man.cgi?section=5&topic=mmdf)
- A specification of MMDF format from the documentation of tin, a newsreader. 
- [MMDF](https://en.wikipedia.org/wiki/MMDF)
- A Wikipedia article describing the Multichannel Memorandum Distribution Facility. 

`Message` objects[¶](#message-objects)

- 
*class*mailbox.Message(*message=None*)[¶](#mailbox.Message)
- A subclass of the - `email.message`- `Message`- `mailbox.Message`add mailbox-format-specific state and behavior.- If - *message*is omitted, the new instance is created in a default, empty state. If- *message*is an- `email.message.Message`- *message*is a- `Message`instance. If- *message*is a string, a byte string, or a file, it should contain an- **RFC 5322**- The format-specific state and behaviors offered by subclasses vary, but in general it is only the properties that are not specific to a particular mailbox that are supported (although presumably the properties are specific to a particular mailbox format). For example, file offsets for single-file mailbox formats and file names for directory-based mailbox formats are not retained, because they are only applicable to the original mailbox. But state such as whether a message has been read by the user or marked as important is retained, because it applies to the message itself. - There is no requirement that - `Message`instances be used to represent messages retrieved using- `Mailbox`- `Message`representations might not be acceptable. For such situations,- `Mailbox`instances also offer string and file-like representations, and a custom message factory may be specified when a- `Mailbox`instance is initialized.

`MaildirMessage` objects[¶](#maildirmessage-objects)

- 
*class*mailbox.MaildirMessage(*message=None*)[¶](#mailbox.MaildirMessage)
- A message with Maildir-specific behaviors. Parameter - *message*has the same meaning as with the- `Message`- Typically, a mail user agent application moves all of the messages in the - `new`subdirectory to the- `cur`subdirectory after the first time the user opens and closes the mailbox, recording that the messages are old whether or not they’ve actually been read. Each message in- `cur`has an “info” section added to its file name to store information about its state. (Some mail readers may also add an “info” section to messages in- `new`.) The “info” section may take one of two forms: it may contain “2,” followed by a list of standardized flags (e.g., “2,FR”) or it may contain “1,” followed by so-called experimental information. Standard flags for Maildir messages are as follows:- Flag - Meaning - Explanation - D - Draft - Under composition - F - Flagged - Marked as important - P - Passed - Forwarded, resent, or bounced - R - Replied - Replied to - S - Seen - Read - T - Trashed - Marked for subsequent deletion - `MaildirMessage`instances offer the following methods:- 
get_subdir()[¶](#mailbox.MaildirMessage.get_subdir)
- Return either “new” (if the message should be stored in the - `new`subdirectory) or “cur” (if the message should be stored in the- `cur`subdirectory).- Note - A message is typically moved from - `new`to- `cur`after its mailbox has been accessed, whether or not the message has been read. A message- `msg`has been read if- `"S" in msg.get_flags()`is- `True`.
 - 
set_subdir(*subdir*)[¶](#mailbox.MaildirMessage.set_subdir)
- Set the subdirectory the message should be stored in. Parameter - *subdir*must be either “new” or “cur”.
 - 
get_flags()[¶](#mailbox.MaildirMessage.get_flags)
- Return a string specifying the flags that are currently set. If the message complies with the standard Maildir format, the result is the concatenation in alphabetical order of zero or one occurrence of each of - `'D'`,- `'F'`,- `'P'`,- `'R'`,- `'S'`, and- `'T'`. The empty string is returned if no flags are set or if “info” contains experimental semantics.
 - 
set_flags(*flags*)[¶](#mailbox.MaildirMessage.set_flags)
- Set the flags specified by - *flags*and unset all others.
 - 
add_flag(*flag*)[¶](#mailbox.MaildirMessage.add_flag)
- Set the flag(s) specified by - *flag*without changing other flags. To add more than one flag at a time,- *flag*may be a string of more than one character. The current “info” is overwritten whether or not it contains experimental information rather than flags.
 - 
remove_flag(*flag*)[¶](#mailbox.MaildirMessage.remove_flag)
- Unset the flag(s) specified by - *flag*without changing other flags. To remove more than one flag at a time,- *flag*may be a string of more than one character. If “info” contains experimental information rather than flags, the current “info” is not modified.
 - 
get_date()[¶](#mailbox.MaildirMessage.get_date)
- Return the delivery date of the message as a floating-point number representing seconds since the epoch. 
 - 
set_date(*date*)[¶](#mailbox.MaildirMessage.set_date)
- Set the delivery date of the message to - *date*, a floating-point number representing seconds since the epoch.
 - 
get_info()[¶](#mailbox.MaildirMessage.get_info)
- Return a string containing the “info” for a message. This is useful for accessing and modifying “info” that is experimental (i.e., not a list of flags). 
 - 
set_info(*info*)[¶](#mailbox.MaildirMessage.set_info)
- Set “info” to - *info*, which should be a string.
 
- 
get_subdir()

When a `MaildirMessage` instance is created based upon an
[ mboxMessage](#mailbox.mboxMessage) or 

[instance, the](#mailbox.MMDFMessage)

`MMDFMessage`*Status*and

*X-Status*headers are omitted and the following conversions take place:

| Resulting state | 
 state`MMDFMessage` | 
|---|---|
| “cur” subdirectory | O flag | 
| F flag | F flag | 
| R flag | A flag | 
| S flag | R flag | 
| T flag | D flag | 

When a `MaildirMessage` instance is created based upon an
[ MHMessage](#mailbox.MHMessage) instance, the following conversions take place:

| Resulting state | 
 | 
|---|---|
| “cur” subdirectory | “unseen” sequence | 
| “cur” subdirectory and S flag | no “unseen” sequence | 
| F flag | “flagged” sequence | 
| R flag | “replied” sequence | 

When a `MaildirMessage` instance is created based upon a
[ BabylMessage](#mailbox.BabylMessage) instance, the following conversions take place:

| Resulting state | 
 | 
|---|---|
| “cur” subdirectory | “unseen” label | 
| “cur” subdirectory and S flag | no “unseen” label | 
| P flag | “forwarded” or “resent” label | 
| R flag | “answered” label | 
| T flag | “deleted” label | 

`mboxMessage` objects[¶](#mboxmessage-objects)

- 
*class*mailbox.mboxMessage(*message=None*)[¶](#mailbox.mboxMessage)
- A message with mbox-specific behaviors. Parameter - *message*has the same meaning as with the- `Message`- Messages in an mbox mailbox are stored together in a single file. The sender’s envelope address and the time of delivery are typically stored in a line beginning with “From “ that is used to indicate the start of a message, though there is considerable variation in the exact format of this data among mbox implementations. Flags that indicate the state of the message, such as whether it has been read or marked as important, are typically stored in - *Status*and- *X-Status*headers.- Conventional flags for mbox messages are as follows: - Flag - Meaning - Explanation - R - Read - Read - O - Old - Previously detected by MUA - D - Deleted - Marked for subsequent deletion - F - Flagged - Marked as important - A - Answered - Replied to - The “R” and “O” flags are stored in the - *Status*header, and the “D”, “F”, and “A” flags are stored in the- *X-Status*header. The flags and headers typically appear in the order mentioned.- `mboxMessage`instances offer the following methods:- 
get_from()[¶](#mailbox.mboxMessage.get_from)
- Return a string representing the “From “ line that marks the start of the message in an mbox mailbox. The leading “From “ and the trailing newline are excluded. 
 - 
set_from(*from_*,*time_=None*)[¶](#mailbox.mboxMessage.set_from)
- Set the “From “ line to - *from_*, which should be specified without a leading “From “ or trailing newline. For convenience,- *time_*may be specified and will be formatted appropriately and appended to- *from_*. If- *time_*is specified, it should be a- `time.struct_time`- `time.strftime()`- `True`(to use- `time.gmtime()`
 - 
get_flags()[¶](#mailbox.mboxMessage.get_flags)
- Return a string specifying the flags that are currently set. If the message complies with the conventional format, the result is the concatenation in the following order of zero or one occurrence of each of - `'R'`,- `'O'`,- `'D'`,- `'F'`, and- `'A'`.
 - 
set_flags(*flags*)[¶](#mailbox.mboxMessage.set_flags)
- Set the flags specified by - *flags*and unset all others. Parameter- *flags*should be the concatenation in any order of zero or more occurrences of each of- `'R'`,- `'O'`,- `'D'`,- `'F'`, and- `'A'`.
 - 
add_flag(*flag*)[¶](#mailbox.mboxMessage.add_flag)
- Set the flag(s) specified by - *flag*without changing other flags. To add more than one flag at a time,- *flag*may be a string of more than one character.
 - 
remove_flag(*flag*)[¶](#mailbox.mboxMessage.remove_flag)
- Unset the flag(s) specified by - *flag*without changing other flags. To remove more than one flag at a time,- *flag*may be a string of more than one character.
 
- 
get_from()

When an `mboxMessage` instance is created based upon a
[ MaildirMessage](#mailbox.MaildirMessage) instance, a “From “ line is generated based upon the

`MaildirMessage` instance’s delivery date, and the following conversions
take place:| Resulting state | 
 | 
|---|---|
| R flag | S flag | 
| O flag | “cur” subdirectory | 
| D flag | T flag | 
| F flag | F flag | 
| A flag | R flag | 

When an `mboxMessage` instance is created based upon an
[ MHMessage](#mailbox.MHMessage) instance, the following conversions take place:

| Resulting state | 
 | 
|---|---|
| R flag and O flag | no “unseen” sequence | 
| O flag | “unseen” sequence | 
| F flag | “flagged” sequence | 
| A flag | “replied” sequence | 

When an `mboxMessage` instance is created based upon a
[ BabylMessage](#mailbox.BabylMessage) instance, the following conversions take place:

| Resulting state | 
 | 
|---|---|
| R flag and O flag | no “unseen” label | 
| O flag | “unseen” label | 
| D flag | “deleted” label | 
| A flag | “answered” label | 

When a `mboxMessage` instance is created based upon an
[ MMDFMessage](#mailbox.MMDFMessage)
instance, the “From “ line is copied and all flags directly correspond:

| Resulting state | 
 | 
|---|---|
| R flag | R flag | 
| O flag | O flag | 
| D flag | D flag | 
| F flag | F flag | 
| A flag | A flag | 

`MHMessage` objects[¶](#mhmessage-objects)

- 
*class*mailbox.MHMessage(*message=None*)[¶](#mailbox.MHMessage)
- A message with MH-specific behaviors. Parameter - *message*has the same meaning as with the- `Message`- MH messages do not support marks or flags in the traditional sense, but they do support sequences, which are logical groupings of arbitrary messages. Some mail reading programs (although not the standard - **mh**and- **nmh**) use sequences in much the same way flags are used with other formats, as follows:- Sequence - Explanation - unseen - Not read, but previously detected by MUA - replied - Replied to - flagged - Marked as important - `MHMessage`instances offer the following methods:- 
get_sequences()[¶](#mailbox.MHMessage.get_sequences)
- Return a list of the names of sequences that include this message. 
 - 
set_sequences(*sequences*)[¶](#mailbox.MHMessage.set_sequences)
- Set the list of sequences that include this message. 
 - 
add_sequence(*sequence*)[¶](#mailbox.MHMessage.add_sequence)
- Add - *sequence*to the list of sequences that include this message.
 - 
remove_sequence(*sequence*)[¶](#mailbox.MHMessage.remove_sequence)
- Remove - *sequence*from the list of sequences that include this message.
 
- 
get_sequences()

When an `MHMessage` instance is created based upon a
[ MaildirMessage](#mailbox.MaildirMessage) instance, the following conversions take place:

| Resulting state | 
 | 
|---|---|
| “unseen” sequence | no S flag | 
| “replied” sequence | R flag | 
| “flagged” sequence | F flag | 

When an `MHMessage` instance is created based upon an
[ mboxMessage](#mailbox.mboxMessage) or 

[instance, the](#mailbox.MMDFMessage)

`MMDFMessage`*Status*and

*X-Status*headers are omitted and the following conversions take place:

| Resulting state | 
 state`MMDFMessage` | 
|---|---|
| “unseen” sequence | no R flag | 
| “replied” sequence | A flag | 
| “flagged” sequence | F flag | 

When an `MHMessage` instance is created based upon a
[ BabylMessage](#mailbox.BabylMessage) instance, the following conversions take place:

| Resulting state | 
 | 
|---|---|
| “unseen” sequence | “unseen” label | 
| “replied” sequence | “answered” label | 

`BabylMessage` objects[¶](#babylmessage-objects)

- 
*class*mailbox.BabylMessage(*message=None*)[¶](#mailbox.BabylMessage)
- A message with Babyl-specific behaviors. Parameter - *message*has the same meaning as with the- `Message`- Certain message labels, called - *attributes*, are defined by convention to have special meanings. The attributes are as follows:- Label - Explanation - unseen - Not read, but previously detected by MUA - deleted - Marked for subsequent deletion - filed - Copied to another file or mailbox - answered - Replied to - forwarded - Forwarded - edited - Modified by the user - resent - Resent - By default, Rmail displays only visible headers. The - `BabylMessage`class, though, uses the original headers because they are more complete. Visible headers may be accessed explicitly if desired.- `BabylMessage`instances offer the following methods:- 
get_labels()[¶](#mailbox.BabylMessage.get_labels)
- Return a list of labels on the message. 
 - 
set_labels(*labels*)[¶](#mailbox.BabylMessage.set_labels)
- Set the list of labels on the message to - *labels*.
 - 
add_label(*label*)[¶](#mailbox.BabylMessage.add_label)
- Add - *label*to the list of labels on the message.
 - 
remove_label(*label*)[¶](#mailbox.BabylMessage.remove_label)
- Remove - *label*from the list of labels on the message.
 - 
get_visible()[¶](#mailbox.BabylMessage.get_visible)
- Return a - `Message`
 - 
set_visible(*visible*)[¶](#mailbox.BabylMessage.set_visible)
- Set the message’s visible headers to be the same as the headers in - *message*. Parameter- *visible*should be a- `Message`- `email.message.Message`
 - 
update_visible()[¶](#mailbox.BabylMessage.update_visible)
- When a - `BabylMessage`instance’s original headers are modified, the visible headers are not automatically modified to correspond. This method updates the visible headers as follows: each visible header with a corresponding original header is set to the value of the original header, each visible header without a corresponding original header is removed, and any of- *Date*,- *From*,- *Reply-To*,- *To*,- *CC*, and- *Subject*that are present in the original headers but not the visible headers are added to the visible headers.
 
- 
get_labels()

When a `BabylMessage` instance is created based upon a
[ MaildirMessage](#mailbox.MaildirMessage) instance, the following conversions take place:

| Resulting state | 
 | 
|---|---|
| “unseen” label | no S flag | 
| “deleted” label | T flag | 
| “answered” label | R flag | 
| “forwarded” label | P flag | 

When a `BabylMessage` instance is created based upon an
[ mboxMessage](#mailbox.mboxMessage) or 

[instance, the](#mailbox.MMDFMessage)

`MMDFMessage`*Status*and

*X-Status*headers are omitted and the following conversions take place:

| Resulting state | 
 state`MMDFMessage` | 
|---|---|
| “unseen” label | no R flag | 
| “deleted” label | D flag | 
| “answered” label | A flag | 

When a `BabylMessage` instance is created based upon an
[ MHMessage](#mailbox.MHMessage) instance, the following conversions take place:

| Resulting state | 
 | 
|---|---|
| “unseen” label | “unseen” sequence | 
| “answered” label | “replied” sequence | 

`MMDFMessage` objects[¶](#mmdfmessage-objects)

- 
*class*mailbox.MMDFMessage(*message=None*)[¶](#mailbox.MMDFMessage)
- A message with MMDF-specific behaviors. Parameter - *message*has the same meaning as with the- `Message`- As with message in an mbox mailbox, MMDF messages are stored with the sender’s address and the delivery date in an initial line beginning with “From “. Likewise, flags that indicate the state of the message are typically stored in - *Status*and- *X-Status*headers.- Conventional flags for MMDF messages are identical to those of mbox message and are as follows: - Flag - Meaning - Explanation - R - Read - Read - O - Old - Previously detected by MUA - D - Deleted - Marked for subsequent deletion - F - Flagged - Marked as important - A - Answered - Replied to - The “R” and “O” flags are stored in the - *Status*header, and the “D”, “F”, and “A” flags are stored in the- *X-Status*header. The flags and headers typically appear in the order mentioned.- `MMDFMessage`instances offer the following methods, which are identical to those offered by- `mboxMessage`- 
get_from()[¶](#mailbox.MMDFMessage.get_from)
- Return a string representing the “From “ line that marks the start of the message in an mbox mailbox. The leading “From “ and the trailing newline are excluded. 
 - 
set_from(*from_*,*time_=None*)[¶](#mailbox.MMDFMessage.set_from)
- Set the “From “ line to - *from_*, which should be specified without a leading “From “ or trailing newline. For convenience,- *time_*may be specified and will be formatted appropriately and appended to- *from_*. If- *time_*is specified, it should be a- `time.struct_time`- `time.strftime()`- `True`(to use- `time.gmtime()`
 - 
get_flags()[¶](#mailbox.MMDFMessage.get_flags)
- Return a string specifying the flags that are currently set. If the message complies with the conventional format, the result is the concatenation in the following order of zero or one occurrence of each of - `'R'`,- `'O'`,- `'D'`,- `'F'`, and- `'A'`.
 - 
set_flags(*flags*)[¶](#mailbox.MMDFMessage.set_flags)
- Set the flags specified by - *flags*and unset all others. Parameter- *flags*should be the concatenation in any order of zero or more occurrences of each of- `'R'`,- `'O'`,- `'D'`,- `'F'`, and- `'A'`.
 - 
add_flag(*flag*)[¶](#mailbox.MMDFMessage.add_flag)
- Set the flag(s) specified by - *flag*without changing other flags. To add more than one flag at a time,- *flag*may be a string of more than one character.
 - 
remove_flag(*flag*)[¶](#mailbox.MMDFMessage.remove_flag)
- Unset the flag(s) specified by - *flag*without changing other flags. To remove more than one flag at a time,- *flag*may be a string of more than one character.
 
- 
get_from()

When an `MMDFMessage` instance is created based upon a
[ MaildirMessage](#mailbox.MaildirMessage) instance, a “From “ line is generated based upon the

`MaildirMessage` instance’s delivery date, and the following conversions
take place:| Resulting state | 
 | 
|---|---|
| R flag | S flag | 
| O flag | “cur” subdirectory | 
| D flag | T flag | 
| F flag | F flag | 
| A flag | R flag | 

When an `MMDFMessage` instance is created based upon an
[ MHMessage](#mailbox.MHMessage) instance, the following conversions take place:

| Resulting state | 
 | 
|---|---|
| R flag and O flag | no “unseen” sequence | 
| O flag | “unseen” sequence | 
| F flag | “flagged” sequence | 
| A flag | “replied” sequence | 

When an `MMDFMessage` instance is created based upon a
[ BabylMessage](#mailbox.BabylMessage) instance, the following conversions take place:

| Resulting state | 
 | 
|---|---|
| R flag and O flag | no “unseen” label | 
| O flag | “unseen” label | 
| D flag | “deleted” label | 
| A flag | “answered” label | 

When an `MMDFMessage` instance is created based upon an
[ mboxMessage](#mailbox.mboxMessage) instance, the “From “ line is copied and all flags directly
correspond:

| Resulting state | 
 | 
|---|---|
| R flag | R flag | 
| O flag | O flag | 
| D flag | D flag | 
| F flag | F flag | 
| A flag | A flag | 

## Exceptions[¶](#exceptions)

The following exception classes are defined in the `mailbox` module:

- 
*exception*mailbox.Error[¶](#mailbox.Error)
- The base class for all other module-specific exceptions. 

- 
*exception*mailbox.NoSuchMailboxError[¶](#mailbox.NoSuchMailboxError)
- Raised when a mailbox is expected but is not found, such as when instantiating a - `Mailbox`- *create*parameter set to- `False`), or when opening a folder that does not exist.

- 
*exception*mailbox.NotEmptyError[¶](#mailbox.NotEmptyError)
- Raised when a mailbox is not empty but is expected to be, such as when deleting a folder that contains messages. 

- 
*exception*mailbox.ExternalClashError[¶](#mailbox.ExternalClashError)
- Raised when some mailbox-related condition beyond the control of the program causes it to be unable to proceed, such as when failing to acquire a lock that another program already holds, or when a uniquely generated file name already exists. 

## Examples[¶](#examples)

A simple example of printing the subjects of all messages in a mailbox that seem interesting:

```
import mailbox
for message in mailbox.mbox('~/mbox'):
    subject = message['subject']       # Could possibly be None.
    if subject and 'python' in subject.lower():
        print(subject)
```
To copy all mail from a Babyl mailbox to an MH mailbox, converting all of the format-specific information that can be converted:

```
import mailbox
destination = mailbox.MH('~/Mail')
destination.lock()
for message in mailbox.Babyl('~/RMAIL'):
    destination.add(mailbox.MHMessage(message))
destination.flush()
destination.unlock()
```
This example sorts mail from several mailing lists into different mailboxes, being careful to avoid mail corruption due to concurrent modification by other programs, mail loss due to interruption of the program, or premature termination due to malformed messages in the mailbox:

```
import mailbox
import email.errors
list_names = ('python-list', 'python-dev', 'python-bugs')
boxes = {name: mailbox.mbox('~/email/%s' % name) for name in list_names}
inbox = mailbox.Maildir('~/Maildir', factory=None)
for key in inbox.iterkeys():
    try:
        message = inbox[key]
    except email.errors.MessageParseError:
        continue                # The message is malformed. Just leave it.
    for name in list_names:
        list_id = message['list-id']
        if list_id and name in list_id:
            # Get mailbox to use
            box = boxes[name]
            # Write copy to disk before removing original.
            # If there's a crash, you might duplicate a message, but
            # that's better than losing a message completely.
            box.lock()
            box.add(message)
            box.flush()
            box.unlock()
            # Remove original message
            inbox.lock()
            inbox.discard(key)
            inbox.flush()
            inbox.unlock()
            break               # Found destination, so stop looking.
for box in boxes.itervalues():
    box.close()
```
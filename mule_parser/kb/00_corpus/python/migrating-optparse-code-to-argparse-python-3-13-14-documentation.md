# Migrating optparse code to argparse — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/howto/argparse-optparse.html](https://docs.python.org/3.13/howto/argparse-optparse.html)

---

# Migrating `optparse` code to `argparse`[¶](#migrating-optparse-code-to-argparse)

The [ argparse](../library/argparse.html#module-argparse) module offers several higher level features not natively
provided by the 

[module, including:](../library/optparse.html#module-optparse)

`optparse`- Handling positional arguments. 
- Supporting subcommands. 
- Allowing alternative option prefixes like - `+`and- `/`.
- Handling zero-or-more and one-or-more style arguments. 
- Producing more informative usage messages. 
- Providing a much simpler interface for custom - `type`and- `action`.

Originally, the [ argparse](../library/argparse.html#module-argparse) module attempted to maintain compatibility
with 

[. However, the fundamental design differences between supporting declarative command line option processing (while leaving positional argument processing to application code), and supporting both named options and positional arguments in the declarative interface mean that the API has diverged from that of](../library/optparse.html#module-optparse)

`optparse``optparse` over time.As described in [Choosing an argument parsing library](../library/optparse.html#choosing-an-argument-parser), applications that are
currently using [ optparse](../library/optparse.html#module-optparse) and are happy with the way it works can
just continue to use 

`optparse`.Application developers that are considering migrating should also review the list of intrinsic behavioural differences described in that section before deciding whether or not migration is desirable.

For applications that do choose to migrate from [ optparse](../library/optparse.html#module-optparse) to 

[, the following suggestions should be helpful:](../library/argparse.html#module-argparse)

`argparse`- Replace all - `optparse.OptionParser.add_option()`- `ArgumentParser.add_argument()`
- Replace - `(options, args) = parser.parse_args()`with- `args = parser.parse_args()`and add additional- `ArgumentParser.add_argument()`- `options`, now in the- `argparse`- `args`.
- Replace - `optparse.OptionParser.disable_interspersed_args()`- `parse_intermixed_args()`- `parse_args()`
- Replace callback actions and the - `callback_*`keyword arguments with- `type`or- `action`arguments.
- Replace string names for - `type`keyword arguments with the corresponding type objects (e.g. int, float, complex, etc).
- Replace - `optparse.Values`- `Namespace`- `optparse.OptionError`- `optparse.OptionValueError`- `ArgumentError`
- Replace strings with implicit arguments such as - `%default`or- `%prog`with the standard Python syntax to use dictionaries to format strings, that is,- `%(default)s`and- `%(prog)s`.
- Replace the OptionParser constructor - `version`argument with a call to- `parser.add_argument('--version', action='version', version='<the version>')`.
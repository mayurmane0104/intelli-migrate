# textwrap — Text wrapping and filling — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/textwrap.html](https://docs.python.org/library/textwrap.html)

---

`textwrap` — Text wrapping and filling[¶](#module-textwrap)

**Source code:** [Lib/textwrap.py](https://github.com/python/cpython/tree/3.14/Lib/textwrap.py)

The `textwrap` module provides some convenience functions,
as well as [ TextWrapper](#textwrap.TextWrapper), the class that does all the work.
If you’re just wrapping or filling one or two text strings, the convenience
functions should be good enough; otherwise, you should use an instance of

`TextWrapper` for efficiency.- 
textwrap.wrap(*text*,*width=70*,***,*initial_indent=''*,*subsequent_indent=''*,*expand_tabs=True*,*replace_whitespace=True*,*fix_sentence_endings=False*,*break_long_words=True*,*drop_whitespace=True*,*break_on_hyphens=True*,*tabsize=8*,*max_lines=None*,*placeholder=' [...]'*)[¶](#textwrap.wrap)
- Wraps the single paragraph in - *text*(a string) so every line is at most- *width*characters long. Returns a list of output lines, without final newlines.- Optional keyword arguments correspond to the instance attributes of - `TextWrapper`- See the - `TextWrapper.wrap()`- `wrap()`behaves.

- 
textwrap.fill(*text*,*width=70*,***,*initial_indent=''*,*subsequent_indent=''*,*expand_tabs=True*,*replace_whitespace=True*,*fix_sentence_endings=False*,*break_long_words=True*,*drop_whitespace=True*,*break_on_hyphens=True*,*tabsize=8*,*max_lines=None*,*placeholder=' [...]'*)[¶](#textwrap.fill)
- Wraps the single paragraph in - *text*, and returns a single string containing the wrapped paragraph.- `fill()`is shorthand for- "\n".join(wrap(text, ...)) - In particular, - `fill()`accepts exactly the same keyword arguments as- `wrap()`

- 
textwrap.shorten(*text*,*width*,***,*fix_sentence_endings=False*,*break_long_words=True*,*break_on_hyphens=True*,*placeholder=' [...]'*)[¶](#textwrap.shorten)
- Collapse and truncate the given - *text*to fit in the given- *width*.- First the whitespace in - *text*is collapsed (all whitespace is replaced by single spaces). If the result fits in the- *width*, it is returned. Otherwise, enough words are dropped from the end so that the remaining words plus the- *placeholder*fit within- *width*:- >>> textwrap.shorten("Hello world!", width=12) 'Hello world!' >>> textwrap.shorten("Hello world!", width=11) 'Hello [...]' >>> textwrap.shorten("Hello world", width=10, placeholder="...") 'Hello...' - Optional keyword arguments correspond to the instance attributes of - `TextWrapper`- `TextWrapper`- `fill()`- `tabsize`- `expand_tabs`- `drop_whitespace`- `replace_whitespace`- Added in version 3.4. 

- 
textwrap.dedent(*text*)[¶](#textwrap.dedent)
- Remove any common leading whitespace from every line in - *text*.- This can be used to make triple-quoted strings line up with the left edge of the display, while still presenting them in the source code in indented form. - Note that tabs and spaces are both treated as whitespace, but they are not equal: the lines - `" hello"`and- `"\thello"`are considered to have no common leading whitespace.- Lines containing only whitespace are ignored in the input and normalized to a single newline character in the output. - For example: - def test(): # end first line with \ to avoid the empty line! s = '''\ hello world ''' print(repr(s)) # prints ' hello\n world\n ' print(repr(dedent(s))) # prints 'hello\n world\n' - Changed in version 3.14: The - `dedent()`function now correctly normalizes blank lines containing only whitespace characters. Previously, the implementation only normalized blank lines containing tabs and spaces.

- 
textwrap.indent(*text*,*prefix*,*predicate=None*)[¶](#textwrap.indent)
- Add - *prefix*to the beginning of selected lines in- *text*.- Lines are separated by calling - `text.splitlines(True)`.- By default, - *prefix*is added to all lines that do not consist solely of whitespace (including any line endings).- For example: - >>> s = 'hello\n\n \nworld' >>> indent(s, ' ') ' hello\n\n \n world' - The optional - *predicate*argument can be used to control which lines are indented. For example, it is easy to add- *prefix*to even empty and whitespace-only lines:- >>> print(indent(s, '+ ', lambda line: True)) + hello + + + world - Added in version 3.3. 

[ wrap()](#textwrap.wrap), 

[and](#textwrap.fill)

`fill()`[work by creating a](#textwrap.shorten)

`shorten()`[instance and calling a single method on it. That instance is not reused, so for applications that process many text strings using](#textwrap.TextWrapper)

`TextWrapper``wrap()` and/or `fill()`, it may be more efficient to
create your own `TextWrapper` object.Text is preferably wrapped on whitespaces and right after the hyphens in
hyphenated words; only then will long words be broken if necessary, unless
[ TextWrapper.break_long_words](#textwrap.TextWrapper.break_long_words) is set to false.

- 
*class*textwrap.TextWrapper(***kwargs*)[¶](#textwrap.TextWrapper)
- The - `TextWrapper`constructor accepts a number of optional keyword arguments. Each keyword argument corresponds to an instance attribute, so for example- wrapper = TextWrapper(initial_indent="* ") - is the same as - wrapper = TextWrapper() wrapper.initial_indent = "* " - You can reuse the same - `TextWrapper`object many times, and you can change any of its options through direct assignment to instance attributes between uses.- The - `TextWrapper`instance attributes (and keyword arguments to the constructor) are as follows:- 
width[¶](#textwrap.TextWrapper.width)
- (default: - `70`) The maximum length of wrapped lines. As long as there are no individual words in the input text longer than- `width`- `TextWrapper`guarantees that no output line will be longer than- `width`characters.
 - 
expand_tabs[¶](#textwrap.TextWrapper.expand_tabs)
- (default: - `True`) If true, then all tab characters in- *text*will be expanded to spaces using the- `expandtabs()`- *text*.
 - 
tabsize[¶](#textwrap.TextWrapper.tabsize)
- (default: - `8`) If- `expand_tabs`- *text*will be expanded to zero or more spaces, depending on the current column and the given tab size.- Added in version 3.3. 
 - 
replace_whitespace[¶](#textwrap.TextWrapper.replace_whitespace)
- (default: - `True`) If true, after tab expansion but before wrapping, the- `wrap()`- `'\t\n\v\f\r'`).- Note - If - `expand_tabs`- `replace_whitespace`- *not*the same as tab expansion.- Note - If - `replace_whitespace`- `str.splitlines()`
 - 
drop_whitespace[¶](#textwrap.TextWrapper.drop_whitespace)
- (default: - `True`) If true, whitespace at the beginning and ending of every line (after wrapping but before indenting) is dropped. Whitespace at the beginning of the paragraph, however, is not dropped if non-whitespace follows it. If whitespace being dropped takes up an entire line, the whole line is dropped.
 - 
initial_indent[¶](#textwrap.TextWrapper.initial_indent)
- (default: - `''`) String that will be prepended to the first line of wrapped output. Counts towards the length of the first line. The empty string is not indented.
 - 
subsequent_indent[¶](#textwrap.TextWrapper.subsequent_indent)
- (default: - `''`) String that will be prepended to all lines of wrapped output except the first. Counts towards the length of each line except the first.
 - 
fix_sentence_endings[¶](#textwrap.TextWrapper.fix_sentence_endings)
- (default: - `False`) If true,- `TextWrapper`attempts to detect sentence endings and ensure that sentences are always separated by exactly two spaces. This is generally desired for text in a monospaced font. However, the sentence detection algorithm is imperfect: it assumes that a sentence ending consists of a lowercase letter followed by one of- `'.'`,- `'!'`, or- `'?'`, possibly followed by one of- `'"'`or- `"'"`, followed by a space. One problem with this algorithm is that it is unable to detect the difference between “Dr.” in- [...] Dr. Frankenstein's monster [...] - and “Spot.” in - [...] See Spot. See Spot run [...] - `fix_sentence_endings`- Since the sentence detection algorithm relies on - `string.lowercase`for the definition of “lowercase letter”, and a convention of using two spaces after a period to separate sentences on the same line, it is specific to English-language texts.
 - 
break_long_words[¶](#textwrap.TextWrapper.break_long_words)
- (default: - `True`) If true, then words longer than- `width`- `width`. If it is false, long words will not be broken, and some lines may be longer than- `width`. (Long words will be put on a line by themselves, in order to minimize the amount by which- `width`is exceeded.)
 - 
break_on_hyphens[¶](#textwrap.TextWrapper.break_on_hyphens)
- (default: - `True`) If true, wrapping will occur preferably on whitespaces and right after hyphens in compound words, as it is customary in English. If false, only whitespaces will be considered as potentially good places for line breaks, but you need to set- `break_long_words`
 - 
max_lines[¶](#textwrap.TextWrapper.max_lines)
- (default: - `None`) If not- `None`, then the output will contain at most- *max_lines*lines, with- *placeholder*appearing at the end of the output.- Added in version 3.4. 
 - 
placeholder[¶](#textwrap.TextWrapper.placeholder)
- (default: - `' [...]'`) String that will appear at the end of the output text if it has been truncated.- Added in version 3.4. 
 - `TextWrapper`also provides some public methods, analogous to the module-level convenience functions:- 
wrap(*text*)[¶](#textwrap.TextWrapper.wrap)
- Wraps the single paragraph in - *text*(a string) so every line is at most- `width`- `TextWrapper`instance. Returns a list of output lines, without final newlines. If the wrapped output has no content, the returned list is empty.
 - 
fill(*text*)[¶](#textwrap.TextWrapper.fill)
- Wraps the single paragraph in - *text*, and returns a single string containing the wrapped paragraph.
 
- 
width
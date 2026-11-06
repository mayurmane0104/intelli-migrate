# Substring - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/substring-function.html](https://docs.aws.amazon.com/quick/latest/userguide/substring-function.html)

---

`substring` returns the characters in a string, starting at the
				location specified by the *start* argument and proceeding for the
				number of characters specified by the *length* arguments. 

## Syntax

				`substring(``expression`,`start`,`length`)

## Arguments

				- 
							*expression*
- 
							An expression can be the name of a field that uses the string data type like `address1`, a literal value like`'Unknown'`, or another function like`substring(field_name,1,5)`.
- 
							*start*
- 
							The character location to start from. *start*is inclusive, so the character at the starting position is the first character in the returned value. The minimum value for*start*is 1.
- 
							*length*
- 
							The number of additional characters to include after *start*.*length*is inclusive of*start*, so the last character returned is (*length*- 1) after the starting character.

## Return type

				String

## Example

				The following example returns the 13th through 19th characters in a string. The beginning of the string is index 1, so you begin counting at the first character.

`substring('Fantasy and Science Fiction',13,7)`The following value is returned.

`Science`
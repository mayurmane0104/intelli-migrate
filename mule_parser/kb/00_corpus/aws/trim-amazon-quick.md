# trim - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/trim-function.html](https://docs.aws.amazon.com/quick/latest/userguide/trim-function.html)

---

`trim` removes both preceding and following blank space from a string. 

## Syntax

				`trim(``expression`)

## Arguments

				- 
							*expression*
- 
							The expression must be a string. It can be the name of a field that uses the string data type, a literal value like `'12 Main Street'`, or a call to another function that outputs a string.

## Return type

				String

## Example

				The following example removes the following spaces from a string.

`trim('   Seattle Store #14   ')`For these field values, the following values are returned.

`Seattle Store #14`
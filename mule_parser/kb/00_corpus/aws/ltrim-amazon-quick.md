# Ltrim - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/ltrim-function.html](https://docs.aws.amazon.com/quick/latest/userguide/ltrim-function.html)

---

`ltrim` removes preceding blank space from a string.

## Syntax

				`ltrim(``expression`)

## Arguments

				- 
							*expression*
- 
							The expression must be a string. It can be the name of a field that uses the string data type, a literal value like `'12 Main Street'`, or a call to another function that outputs a string.

## Return type

				String

## Example

				The following example removes the preceding spaces from a string.

`ltrim('   Seattle Store #14')`The following value is returned.

`Seattle Store #14`
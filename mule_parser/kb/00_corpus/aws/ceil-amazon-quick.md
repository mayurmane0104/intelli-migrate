# Ceil - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/ceil-function.html](https://docs.aws.amazon.com/quick/latest/userguide/ceil-function.html)

---

`ceil` rounds a decimal value to the next highest integer. For example,
					`ceil(29.02)` returns `30`.

## Syntax

				`ceil(``decimal`)

## Arguments

				- 
							*decimal*
- 
							A field that uses the decimal data type, a literal value like `17.62`, or a call to another function that outputs a decimal.

## Return type

				Integer

## Example

				The following example rounds a decimal field to the next highest integer.

`ceil(salesAmount)`The following are the given field values.

```
20.13
892.03
57.54
```
For these field values, the following values are returned.

`21 893 58`
# Floor - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/floor-function.html](https://docs.aws.amazon.com/quick/latest/userguide/floor-function.html)

---

`floor` decrements a decimal value to the next lowest integer. For
				example, `floor(29.08)` returns `29`.

## Syntax

				`floor(``decimal`)

## Arguments

				- 
							*decimal*
- 
							A field that uses the decimal data type, a literal value like `17.62`, or a call to another function that outputs a decimal.

## Return type

				Integer

## Example

				The following example decrements a decimal field to the next lowest integer.

`floor(salesAmount)`The following are the given field values.

```
20.13
892.03
57.54
```
For these field values, the following values are returned.

`20 892 57`
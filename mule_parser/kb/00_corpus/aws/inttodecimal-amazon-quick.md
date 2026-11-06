# intToDecimal - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/intToDecimal-function.html](https://docs.aws.amazon.com/quick/latest/userguide/intToDecimal-function.html)

---

`intToDecimal` converts an integer value to the decimal data
				type.

## Syntax

				`intToDecimal(``integer`)

## Arguments

				- 
							*int*
- 
							A field that uses the integer data type, a literal value like `14`, or a call to another function that outputs an integer.

## Return type

				Decimal(Fixed) in the legacy data preparation experience.

Decimal(Float) in the new data preparation experience.

## Example

				The following example converts an integer field to a decimal.

`intToDecimal(price)`

The following are the given field values.

`20 892 57`

For these field values, the following values are returned.

```
20.0
892.0
58.0
```
You can apply formatting inside an analysis, for example to format
						`price` as currency.
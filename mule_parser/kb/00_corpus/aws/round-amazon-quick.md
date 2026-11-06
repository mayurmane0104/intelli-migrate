# Round - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/round-function.html](https://docs.aws.amazon.com/quick/latest/userguide/round-function.html)

---

`round` rounds a decimal value to the closest integer if no scale is
				specified, or to the closest decimal place if scale is specified.

## Syntax

				`round(`decimal,scale)

## Arguments

				- 
							*decimal*
- 
							A field that uses the decimal data type, a literal value like `17.62`, or a call to another function that outputs a decimal.
- 
							*scale*
- 
							The number of decimal places to use for the return values. 

## Return type

				| Operand | Return type in the legacy data preparation experience | Return type in the new data preparation experience | 
|---|---|---|
| INT | DECIMAL(FIXED) | DECIMAL(FIXED) | 
| DECIMAL(FIXED) | DECIMAL(FIXED) | DECIMAL(FIXED) | 
| DECIMAL(FLOAT) | DECIMAL(FIXED) | DECIMAL(FLOAT) | 

## Example

				The following example rounds a decimal field to the closest second decimal place.

`round(salesAmount, 2)`The following are the given field values.

```
20.1307
892.0388
57.5447
```
For these field values, the following values are returned.

```
20.13
892.04
58.54
```
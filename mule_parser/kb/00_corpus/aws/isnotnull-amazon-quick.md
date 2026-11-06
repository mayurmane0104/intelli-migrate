# isNotNull - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/isNotNull-function.html](https://docs.aws.amazon.com/quick/latest/userguide/isNotNull-function.html)

---

`isNotNull` evaluates an expression to see if it is not null. If the
				expression is not null, `isNotNull` returns true, and otherwise it
				returns false.

## Syntax

				`isNotNull(``expression`)

## Arguments

				- 
							*expression*
- 
							The expression to be evaluated as null or not. It can be a field name like `address1`or a call to another function that outputs a string.

## Return type

				Boolean

## Example

				The following example evaluates the sales_amount field for null values.

`isNotNull(salesAmount)`

The following are the given field values.

```
20.13
(null)
57.54
```
For these field values, the following values are returned.

```
true
false
true
```
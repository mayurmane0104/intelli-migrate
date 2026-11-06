# Operators - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/arithmetic-and-comparison-operators.html](https://docs.aws.amazon.com/quick/latest/userguide/arithmetic-and-comparison-operators.html)

---

You can use the following operators in calculated fields. Quick uses the standard order of operations: parentheses, exponents, multiplication, division, addition, subtraction (PEMDAS). Equal (=) and not equal (<>) comparisons are case-sensitive.

- 
				Addition (+) 
- 
				Subtraction (−) 
- 
				Multiplication (*) 
- 
				Division (/) 
- 
				Modulo (%) – See also `mod()`in the following list.
- 
				Power (^) – See also `exp()`in the following list.
- 
				Equal (=) 
- 
				Not equal (<>) 
- 
				Greater than (>) 
- 
				Greater than or equal to (>=) 
- 
				Less than (<) 
- 
				Less than or equal to (<=) 
- 
				AND 
- 
				OR 
- 
				NOT 

Amazon Quick supports applying the following mathematical functions to an expression.

- 
				[Mod](https://docs.aws.amazon.com/quicksight/latest/user/mod-function.html)(`number`,`divisor`)
- 
				[Log](https://docs.aws.amazon.com/quicksight/latest/user/log-function.html)(`expression`)
- 
				[Ln](https://docs.aws.amazon.com/quicksight/latest/user/ln-function.html)(`expression`)
- 
				[Abs](https://docs.aws.amazon.com/quicksight/latest/user/abs-function.html)(`expression`)
- 
				[Sqrt](https://docs.aws.amazon.com/quicksight/latest/user/sqrt-function.html)(`expression`)
- 
				[Exp](https://docs.aws.amazon.com/quicksight/latest/user/exp-function.html)(`expression`)*e*raised to the power of a given expression.

To make lengthy calculations easier to read, you can use parenthesis to clarify groupings and precedence in calculations. In the following statement, you don't need parentheses. The multiplication statement is processed first, and then the result is added to five, returning a value of 26. However, parentheses make the statement easier to read and thus maintain.

`5 + (7 * 3)`Because parenthesis are first in the order of operations, you can change the order in which other operators are applied. For example, in the following statement the addition statement is processed first, and then the result is multiplied by three, returning a value of 36.

`(5 + 7) * 3`

## Example: Arithmetic operators

			The following example uses multiple arithmetic operators to determine a sales total after discount.

`(Quantity * Amount) - Discount`

## Example: (/) Division

			The following example uses division to divide 3 by 2. A value of 1.5 is returned. Amazon Quick uses floating point divisions.

`3/2`## Example: (=) equal

			Using = performs a case-sensitive comparison of values. Rows where the comparison is TRUE are included in the result set.

In the following example, rows where the `Region` field is
					`South` are included in the results. If the
					`Region` is `south`, these rows are
				excluded.

`Region = 'South'`In the following example, the comparison evaluates to FALSE.

`Region = 'south'`The following example shows a comparison that converts `Region` to
					all uppercase (`SOUTH`), and compares it to
						`SOUTH`. This returns rows where the region is
						`south`, `South`, or
						`SOUTH`.

`toUpper(Region) = 'SOUTH'`## Example: (<>)

			The not equal symbol <> means *less than or
					greater than*. 

So, if we say `x<>1`, then we are saying *if x is less than 1 OR if x is greater than 1*. Both
				< and > are evaluated together. In other words, *if x
					is any value except 1*. Or, *x is not equal to
					1*. 

###### Note

Use <>, not !=.

The following example compares `Status Code` to a numeric value. This
				returns rows where the `Status Code` is not equal to
					`1`.

`statusCode <> 1`The following example compares multiple `statusCode` values. In this
				case, active records have `activeFlag = 1`. This example returns rows
				where one of the following applies:

- 
					For active records, show rows where the status isn't 1 or 2 
- 
					For inactive records, show rows where the status is 99 or -1 

```
( activeFlag = 1 AND (statusCode <> 1 AND statusCode <> 2) )
OR
( activeFlag = 0 AND (statusCode= 99 OR statusCode= -1) )
```
## Example: (^)

			The power symbol `^` means *to the power
					of*. You can use the power operator with any numeric field, with any
				valid exponent. 

The following example is a simple expression of 2 to the power of 4 or (2 * 2 * 2 * 2). This returns a value of 16.

`2^4`The following example computes the square root of the revenue field.

`revenue^0.5`## Example: AND, OR, and NOT

			The following example uses AND, OR, and NOT to compare multiple expressions. It does so using conditional operators to tag top customers NOT in Washington or Oregon with a special promotion, who made more than 10 orders. If no values are returned, the value 'n/a' is used.

`ifelse(( (NOT (State = 'WA' OR State = 'OR')) AND Orders > 10), 'Special Promotion XYZ', 'n/a')`## Example: Creating comparison lists like "in" or "not in"

			This example uses operators to create a comparison to find values that exist, or don't exist, in a specified list of values.

The following example compares `promoCode` a specified list of values.
				This example returns rows where the `promoCode` is in the list
					`(1, 2, 3)`.

```
promoCode    = 1
OR promoCode = 2
OR promoCode = 3
```
The following example compares `promoCode` a specified list of values.
				This example returns rows where the `promoCode` is NOT in the list
					`(1, 2, 3)`.

`NOT(promoCode = 1 OR promoCode = 2 OR promoCode = 3 )`

Another way to express this is to provide a list where the `promoCode`
				is not equal to any items in the list.

```
promoCode     <> 1
AND promoCode <> 2
AND promoCode <> 3
```
## Example: Creating a "between" comparison

			This example uses comparison operators to create a comparison showing values that exist between one value and another.

The following example examines `OrderDate` and returns rows where the
					`OrderDate` is between the first day and last day of 2016. In this
				case, we want the first and last day included, so we use "or equal to" on the
				comparison operators. 

`OrderDate >= "1/1/2016" AND OrderDate <= "12/31/2016"`
# maxIf - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/maxIf-function.html](https://docs.aws.amazon.com/quick/latest/userguide/maxIf-function.html)

---

Based on a conditional statement, the `maxIf` function returns the maximum
			value of the specified measure, grouped by the chosen dimension or dimensions. For
			example, ```
maxIf(ProdRev,CalendarDay >= ${BasePeriodStartDate} AND CalendarDay <=
				${BasePeriodEndDate} AND SourcingType <> 'Indirect')
```
 returns the maximum
			sales goals grouped by the (optional) chosen dimension, if the condition evaluates to
			true.

## Syntax

			`maxIf(`measure, condition)

## Arguments

			- 
						*measure*
- 
						The argument must be a measure. Null values are omitted from the results. Literal values don't work. The argument must be a field. 
- 
						*condition*
- 
						One or more conditions in a single statement.
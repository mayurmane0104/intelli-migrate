# avgIf - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/avgIf-function.html](https://docs.aws.amazon.com/quick/latest/userguide/avgIf-function.html)

---

Based on a conditional statement, the `avgIf` function averages the set of
			numbers in the specified measure, grouped by the chosen dimension or dimensions. For
			example, ```
avgIf(ProdRev,CalendarDay >= ${BasePeriodStartDate} AND CalendarDay <=
				${BasePeriodEndDate} AND SourcingType <> 'Indirect')
```
 returns the average
			for that measure grouped by the (optional) chosen dimension, if the condition evaluates
			to true.

## Syntax

			`avgIf(``dimension or measure, condition`)

## Arguments

			- 
						*decimal*
- 
						The argument must be a measure. Null values are omitted from the results. Literal values don't work. The argument must be a field. 
- 
						*condition*
- 
						One or more conditions in a single statement.
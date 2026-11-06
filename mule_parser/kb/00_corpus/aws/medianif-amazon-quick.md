# medianIf - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/medianIf-function.html](https://docs.aws.amazon.com/quick/latest/userguide/medianIf-function.html)

---

Based on a conditional statement, the `medianIf` aggregation returns the
			median value of the specified measure, grouped by the chosen dimension or dimensions.
			For example, ```
medianIf(Revenue,SaleDate >= ${BasePeriodStartDate} AND SaleDate
				<= ${BasePeriodEndDate})
```
 returns the median revenue grouped by the
			(optional) chosen dimension, if the condition evaluates to true. 

## Syntax

			`medianIf(``measure`,`condition`)

## Arguments

			- 
						*measure*
- 
						The argument must be a measure. Null values are omitted from the results. Literal values don't work. The argument must be a field. 
- 
						*condition*
- 
						One or more conditions in a single statement.
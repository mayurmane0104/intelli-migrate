# varpIf - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/varpIf-function.html](https://docs.aws.amazon.com/quick/latest/userguide/varpIf-function.html)

---

Based on a conditional statement, the `varpIf` function calculates the
			variance of the set of numbers in the specified measure, grouped by the chosen dimension
			or dimensions, based on a biased population.

## Syntax

			`varpIf(`measure, conditions)

## Arguments

			- 
						*measure*
- 
						The argument must be a measure. Null values are omitted from the results. Literal values don't work. The argument must be a field. 
- 
						*condition*
- 
						One or more conditions in a single statement.
# stdevIf - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/stdevIf-function.html](https://docs.aws.amazon.com/quick/latest/userguide/stdevIf-function.html)

---

Based on a conditional statement, the `stdevIf` function calculates the
			standard deviation of the set of numbers in the specified measure, grouped by the chosen
			dimension or dimensions, based on a sample. 

## Syntax

			`stdevIf(`measure, conditions)

## Arguments

			- 
						*measure*
- 
						The argument must be a measure. Null values are omitted from the results. Literal values don't work. The argument must be a field. 
- 
						*condition*
- 
						One or more conditions in a single statement.
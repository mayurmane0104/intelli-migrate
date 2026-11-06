# countIf - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/countIf-function.html](https://docs.aws.amazon.com/quick/latest/userguide/countIf-function.html)

---

Based on a conditional statement, the `countIf` function calculates the
			number of values in a dimension or measure, grouped by the chosen dimension or
			dimensions.

## Syntax

			`countIf(`dimension or measure, condition)

## Arguments

			- 
						*dimension or measure*
- 
						The argument must be a measure or a dimension. Null values are omitted from the results. Literal values don't work. The argument must be a field. 
- 
						*condition*
- 
						One or more conditions in a single statement. 

## Return type

			Integer

## Example

			The following function returns a count of the sales transactions
					(`Revenue`) that meet the conditions, including any duplicates. 

```
countIf (
    Revenue,
    # Conditions
        CalendarDay >= ${BasePeriodStartDate} AND 
        CalendarDay <= ${BasePeriodEndDate} AND 
        SourcingType <> 'Indirect'
)
```
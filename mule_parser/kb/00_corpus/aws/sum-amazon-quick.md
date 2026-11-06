# sum - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/sum-function.html](https://docs.aws.amazon.com/quick/latest/userguide/sum-function.html)

---

The `sum` function adds the set of numbers in the specified measure,
			grouped by the chosen dimension or dimensions. For example, ```
sum(profit
				amount)
```
 returns the total profit amount grouped by the (optional) chosen
			dimension.

## Syntax

			`sum(`measure, [group-by level])

## Arguments

			- 
						*measure*
- 
						The argument must be a measure. Null values are omitted from the results. Literal values don't work. The argument must be a field. 
- 
						*group-by level*
- 
						(Optional) Specifies the level to group the aggregation by. The level added can be any dimension or dimensions independent of the dimensions added to the visual. The argument must be a dimension field. The group-by level must be enclosed in square brackets `[ ]`. For more information, see[Level-aware calculation - aggregate (LAC-A) functions](https://docs.aws.amazon.com/quicksight/latest/user/level-aware-calculations-aggregate.html).

## Examples

			The following example returns the sum of sales.

`sum({Sales})`You can also specify at what level to group the computation using one or more
				dimensions in the view or in your dataset. This is called a LAC-A function. For more
				information about LAC-A functions, see [Level-aware calculation - aggregate (LAC-A)
					functions](https://docs.aws.amazon.com/quicksight/latest/user/level-aware-calculations-aggregate.html). The following example calculates the sum of sales at the
				Country level, but not across other dimensions (Region and Product) in the
				visual.

`sum(Sales, [Country])`![The sum of sales for each country.](/images/quick/latest/userguide/images/sum-function-example.png)
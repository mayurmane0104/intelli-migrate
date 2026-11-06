# min - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/min-function.html](https://docs.aws.amazon.com/quick/latest/userguide/min-function.html)

---

The `min` function returns the minimum value of the specified measure or
			date, grouped by the chosen dimension or dimensions. For example, ```
min(return
				rate)
```
 returns the minimum rate of returns grouped by the (optional) chosen
			dimension.

## Syntax

			`min(`measure, [group-by level])

## Arguments

			- 
						*measure*
- 
						The argument must be a measure or a date. Null values are omitted from the results. Literal values don't work. The argument must be a field. Minimum dates work only in the **Value**field well of tables and pivot tables.
- 
						*group-by level*
- 
						(Optional) Specifies the level to group the aggregation by. The level added can be any dimension or dimensions independent of the dimensions added to the visual. The argument must be a dimension field. The group-by level must be enclosed in square brackets `[ ]`. For more information, see[Level-aware calculation - aggregate (LAC-A) functions](https://docs.aws.amazon.com/quicksight/latest/user/level-aware-calculations-aggregate.html).

## Examples

			The following example returns the minimum sales value for each region. It is compared to the total, max, and median sales.

`min({Sales})`![The minimum sales value for each region.](/images/quick/latest/userguide/images/min-max-median-function-example.png) 

				 
				 
			You can also specify at what level to group the computation using one or more
				dimensions in the view or in your dataset. This is called a LAC-A function. For more
				information about LAC-A functions, see [Level-aware calculation - aggregate (LAC-A)
					functions](https://docs.aws.amazon.com/quicksight/latest/user/level-aware-calculations-aggregate.html). The following example calculates the minimum sales at the
				Country level, but not across other dimensions (Region) in the visual.

`min({Sales}, [Country])`![The minimum sales value in each country.](/images/quick/latest/userguide/images/min-function-example2.png)
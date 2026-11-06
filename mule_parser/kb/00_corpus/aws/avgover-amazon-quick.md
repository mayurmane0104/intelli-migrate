# avgOver - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/avgOver-function.html](https://docs.aws.amazon.com/quick/latest/userguide/avgOver-function.html)

---

The `avgOver` function calculates the average of a measure partitioned by a
			list of dimensions. 

## Syntax

			The brackets are required. To see which arguments are optional, see the following descriptions.

`avgOver (``measure`,`[ partition_field, ... ]`,`calculation level`)

The following example shows the average `Billed Amount` over
					`Customer Region`. The fields in the table calculation are in the
				field wells of the visual.

```
avgOver
(
     sum({Billed Amount}),
     [{Customer Region}]
)
```
The following screenshot shows the results of the example. With the addition of
					`Service Line`, the total amount billed for each is displayed, and
				the average of these three values displays in the calculated field.

![Table showing Billed Amount and avgOver values grouped by Customer Region and Service Line.](/images/quick/latest/userguide/images/avgOver.png) 

				 
				 
			## Arguments

			- 
						*measure*
- 
						The measure that you want to do the calculation for, for example `sum({Sales Amt})`. Use an aggregation if the calculation level is set to`NULL`or`POST_AGG_FILTER`. Don't use an aggregation if the calculation level is set to`PRE_FILTER`or`PRE_AGG`.
- 
						*partition field*
- 
						(Optional) One or more dimensions that you want to partition by, separated by commas. Each field in the list is enclosed in {} (curly braces), if it is more than one word. The entire list is enclosed in [ ] (square brackets). 
- 
						*calculation level*
- 
						(Optional) Specifies the calculation level to use: - 
								`PRE_FILTER`– Prefilter calculations are computed before the dataset filters.
- 
								`PRE_AGG`– Preaggregate calculations are computed before applying aggregations and top and bottom*N*filters to the visuals.
- 
								`POST_AGG_FILTER`– (Default) Table calculations are computed when the visuals display.
 This value defaults to `POST_AGG_FILTER`when blank. For more information, see[Using level-aware calculations in Quick](https://docs.aws.amazon.com/quicksight/latest/user/level-aware-calculations.html).
- 
								

## Example

			The following example gets the average `sum(Sales)` partitioned over
					`City` and `State`. 

```
avgOver
(
     sum(Sales), 
     [City, State]
) 
```
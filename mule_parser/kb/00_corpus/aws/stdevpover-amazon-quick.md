# stdevpOver - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/stdevpOver-function.html](https://docs.aws.amazon.com/quick/latest/userguide/stdevpOver-function.html)

---

The `stdevpOver` function calculates the standard deviation of the
			specified measure, partitioned by the chosen attribute or attributes, based on a biased
			population.

## Syntax

			The brackets are required. To see which arguments are optional, see the following descriptions.

`stdevpOver (``measure`,`[ partition_field, ... ]`,`calculation level`)

## Arguments

			- *measure*
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
								`POST_AGG_FILTER`– (default) table calculations are computed when the visuals display.
 This value defaults to `POST_AGG_FILTER`when blank. For more information, see[Using level-aware calculations in Quick](https://docs.aws.amazon.com/quicksight/latest/user/level-aware-calculations.html).
- 
								

## Example

			The following example calculates the standard deviation of
				`sum(Sales)`, partitioned by `City` and `State`,
				based on a biased population.

```
stdevpOver
(
     sum(Sales), 
     [City, State]
) 
```
The following example calculates the standard deviation of ```
Billed
					Amount
```
 over `Customer Region`, based on a biased population.
				The fields in the table calculation are in the field wells of the visual.

```
stdevpOver
(
     sum({Billed Amount}),
     [{Customer Region}]
)
```
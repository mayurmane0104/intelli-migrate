# denseRank - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/denseRank-function.html](https://docs.aws.amazon.com/quick/latest/userguide/denseRank-function.html)

---

The `denseRank` function calculates the rank of a measure or a dimension in
			comparison to the specified partitions. It counts each item only once, ignoring
			duplicates, and assigns a rank "without holes" so that duplicate values share the same
			rank. 

## Syntax

			The brackets are required. To see which arguments are optional, see the following descriptions.

`denseRank (``[ sort_order_field ASC_or_DESC, ... ]`,`[ partition_field, ... ]`)

## Arguments

			- 
						*sort order field*
- 
						One or more aggregated fields, either measures or dimensions or both, that you want to sort the data by, separated by commas. You can either specify ascending ( `ASC`) or descending (`DESC`) sort order.Each field in the list is enclosed in {} (curly braces), if it is more than one word. The entire list is enclosed in [ ] (square brackets). 
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

			The following example densely ranks `max(Sales)`, based on a descending
				sort order, by `State` and `City`. Any cities with the same
					`max(Sales)` are assigned the same rank, and the next city is ranked
				consecutively after them. For example, if three cities share the same ranking, the
				fourth city is ranked as second. 

```
denseRank
(
  [max(Sales) DESC], 
  [State, City]
)
```
The following example densely ranks `max(Sales)`, based on a descending
				sort order, by `State`. Any states with the same `max(Sales)`
				are assigned the same rank, and the next is ranked consecutively after them. For
				example, if three states share the same ranking, the fourth state is ranked as
				second. 

```
denseRank
(
  [max(Sales) DESC], 
  [State]
)
```
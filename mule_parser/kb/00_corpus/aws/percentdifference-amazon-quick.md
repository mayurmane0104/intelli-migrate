# percentDifference - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/percentDifference-function.html](https://docs.aws.amazon.com/quick/latest/userguide/percentDifference-function.html)

---

The `percentDifference` function calculates the percentage difference
			between the current value and a comparison value, based on partitions, sorts, and lookup
			index. 

## Syntax

			The brackets are required. To see which arguments are optional, see the following descriptions.

`percentDifference (``measure`,`[ sortorder_field ASC_or_DESC, ... ]`,`lookup index`,`[ partition_field, ... ]`)

## Arguments

			- 
						*measure*
- 
						An aggregated measure that you want to see the percent difference for. 
- 
						*sort order field*
- 
						One or more measures and dimensions that you want to sort the data by, separated by commas. You can specify either ascending ( `ASC`) or descending (`DESC`) sort order.Each field in the list is enclosed in {} (curly braces), if it is more than one word. The entire list is enclosed in [ ] (square brackets). 
- 
						*lookup index*
- 
						The lookup index can be positive or negative, indicating a following row in the sort (positive) or a previous row in the sort (negative). The lookup index can be 1–2,147,483,647. For the engines MySQL, MariaDB and Aurora MySQL-Compatible Edition, the lookup index is limited to just 1. 
- 
						*partition field*
- 
						(Optional) One or more dimensions that you want to partition by, separated by commas. Each field in the list is enclosed in {} (curly braces), if it is more than one word. The entire list is enclosed in [ ] (square brackets). 

## Example

			The following example calculates the percentage of difference between the
					`sum(Sales)` for the current and the previous `State`,
				sorted by `Sales`.

```
percentDifference
(
  sum(amount), 
  [sum(amount) ASC],
  -1, 
  [State]
)
```
The following example calculates the percent that a specific ```
Billed
					Amount
```
 is of another `Billed Amount`, sorted by
					(`[{Customer Region} ASC]`). The fields in the table calculation are
				in the field wells of the visual.

```
percentDifference
(
  sum( {Billed Amount} ), 
  [{Customer Region} ASC],
  1
)
```
The following screenshot shows the results of the example. The red letters show
				that the total `Billed Amount` for the `Customer Region`
				`APAC` is 24 percent less than the amount for the
					`EMEA` region.

![Table showing Billed Amount and percentDifference by Customer Region with calculation formula.](/images/quick/latest/userguide/images/percentDifference.png)
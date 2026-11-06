# lead - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/lead-function.html](https://docs.aws.amazon.com/quick/latest/userguide/lead-function.html)

---

The `lead` function calculates the lead (following) value for a measure
			based on specified partitions and sorts.

## Syntax

			The brackets are required. To see which arguments are optional, see the following descriptions.

`lead (``measure ,[ sortorder_field ASC_or_DESC, ... ] ,lookup_index, ,[ partition_field, ... ]`)

## Arguments

			- *measure*
- 
						The measure that you want to get the lead for. This can include an aggregate, for example `sum({Sales Amt})`.
- *sort order field*
- 
						One or more measures and dimensions that you want to sort the data by, separated by commas. You can specify either ascending ( `ASC`) or descending (`DESC`) sort order.Each field in the list is enclosed in {} (curly braces), if it is more than one word. The entire list is enclosed in [ ] (square brackets). 
- *lookup index*
- 
						The lookup index can be positive or negative, indicating a following row in the sort (positive) or a previous row in the sort (negative). The lookup index can be 1–2,147,483,647. For the engines MySQL, MariaDB, and Amazon Aurora MySQL-Compatible Edition, the lookup index is limited to just 1. 
- 
						*partition field*
- 
						(Optional) One or more dimensions that you want to partition by, separated by commas. Each field in the list is enclosed in {} (curly braces), if it is more than one word. The entire list is enclosed in [ ] (square brackets). 

## Example

			The following example calculates the next `sum(sales)`, partitioned by
				the state of origin, in the ascending sort order on
				`cancellation_code`.

```
lead
(
     sum(sales), 
     [cancellation_code ASC], 
     1, 
     [origin_state_nm]
)
```
The following example uses a calculated field with lead to display the amount for
				the next row beside the amount for the current row, sorted by ```
Customer
					Segment
```
. The fields in the table calculation are in the field wells of
				the visual.

```
lead(
     sum({Billed Amount}),
     [{Customer Segment} ASC],
     1
)
```
The following screenshot shows the results of the example.

![Table showing Lead and Sum of Billed Amount by Customer Segment with grouped field wells.](/images/quick/latest/userguide/images/leadCalc.png)
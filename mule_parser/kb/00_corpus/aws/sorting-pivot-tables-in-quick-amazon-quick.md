# Sorting pivot tables in Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/sorting-pivot-tables.html](https://docs.aws.amazon.com/quick/latest/userguide/sorting-pivot-tables.html)

---

In Amazon Quick, you can sort values in a pivot table by fields in the
					**Rows** and **Columns** field wells or
				quickly by column headers in the pivot table. In pivot tables, you can sort rows and
				columns independently of each other in alphabetical order, or by a measure.

###### Note

You can't run Total, Difference, and Percent Difference table calculations
					when a pivot table is being sorted by a measure. For more information about
					using table calculations in pivot tables, see [Using table calculations in pivot tables](./working-with-calculations.html).

## Understanding sorting in pivot tables

				When you have multiple panes in a pivot table, sorting is applied to each pane
					independently. For example, the `Segment` column in the pivot table
					on the left is being sorted in ascending order by `Cost`. Given that
					there are multiple panes, the sort starts over for each pane and the rows within
					each pane (for `Segment`) are ordered by lowest to highest cost. The
					table on the right has the same sort applied, but the sort is being applied
					across the entire table, as shown following.

![Image of a pivot table with a sort highlighted in red.](/images/quick/latest/userguide/images/sorting-pivot-tables2.png) 

					 
					 
				When you apply multiple sorts to a pivot table, sorting is applied from the
					outside dimension to the inside dimension. Consider the following example image
					of a pivot table. The `Customer Region` column is sorted by
						`Cost` in descending order (as shown in orange). The
						`Channel` column is sorted by Revenue Goal in ascending order (as
					shown in blue).

![Image of a pivot table showing two measure value columns sorted.](/images/quick/latest/userguide/images/sorting-pivot-tables3.png) 

					 
					 
				## Sorting pivot tables using row or column headers

				Use the following procedure to sort a pivot table using Row or Column headers.

###### To sort values in a tabular pivot table using table headers

- 
						In a tabular pivot table chart, choose the header that you want to sort. 
- 
						For **Sort by**, choose a field to sort by and a sort order.You can sort dimension fields alphabetically a–z or z–a, or you can sort them by a measure in ascending or descending order. ![Animated .gif file of sorting values in a pivot table using column headers.](/images/quick/latest/userguide/images/sorting-pivot-table7.gif)  

## Sorting pivot tables using value headers

				Use the following procedure to sort a pivot table using value headers.

###### To sort a pivot table using value headers

- 
						In a pivot table chart, choose the value header that you want to sort. 
- 
						Choose **Ascending**or**Descending**.![Animated .gif file of sorting values in a pivot table using value headers.](/images/quick/latest/userguide/images/sorting-pivot-tables-value.gif)  Sorting by value headers in a pivot table also works on subtotals. 

## Sorting tabular pivot tables using the field wells

				Use the following procedure to sort values in a tabular pivot table using the field wells.

###### To sort values in a tabular pivot table using the field wells

- 
						On the analysis page, choose the tabular pivot table that you want to sort. 
- 
						Expand the **Field wells**.
- 
						In the **Rows**or**Columns**field well, choose the field that you want to sort, and then choose how you want to sort the field for**Sort by**.You can sort dimension fields in the **Rows**or**Columns**field wells alphabetically from a–z or z–a, or you can sort them by a measure in ascending or descending order. You also have the option to collapse all or expand all rows or columns for the field you choose in the field well. You can also remove the field, or to replace it with another field.- 
								To sort a dimension field alphabetically, hover your cursor over the field in the **Rows**or**Columns**field well, and then choose the a–z or z–a sort icon.![Image of a field in the Rows field well with the sort by field and alphabetical sort icons indicated in red squares.](/images/quick/latest/userguide/images/sorting-pivot-tables1.png)  
- 
								To sort a dimension field by a measure, hover your cursor over the field in the **Rows**or**Columns**field well. Then choose a measure from the list, and then choose the ascending or descending sort icon.![Image of a field in the Rows field well with the sort by field and sort icons indicated in red squares.](/images/quick/latest/userguide/images/sorting-pivot-tables4.png)  
 
- 
								

Or, if you want more control over how the sort is applied to the pivot table, customize the sort options.

###### To create a sort using the **sort options**

- 
						On the analysis page, choose the pivot table that you want to sort. 
- 
						Expand **Field wells**.
- 
						Choose the field that you want to sort in the **Rows**or**Columns**field well, and then choose**Sort options**.
- 
						In the **Sort options**pane that opens at left, specify the following options:- 
								For **Sort by**, choose a field from the drop-down list.
- 
								For **Aggregation**, choose an aggregation from the list.
- 
								For **Sort order**, select**Ascending**or**Descending**.
- 
								Choose **Apply**.
 
- 
								

## Sorting hierarchy pivot tables using the field wells

				For tabular pivot tables, each field in the **Rows ** field
					well has a separate title cell. For hierarchy pivot tables, all row fields are
					displayed in a single column. To sort, collapse, and expand these row fields,
					select the **Rows** label to open the **Combined row
						fields** menu and choose the option that you want. Each field in a
					hierarchy pivot table can be individually sorted from the **Combined row
						fields** menu.

![Image of the Combined row fields menu.](/images/quick/latest/userguide/images/pivot-table-combined-row-fields-menu.png) 

					 
					 
				More advanced formatting options such as **Hide** and
						**Remove** are available from the field well menus.
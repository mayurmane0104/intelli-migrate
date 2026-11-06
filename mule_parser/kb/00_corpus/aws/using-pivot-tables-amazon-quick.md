# Using pivot tables - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/pivot-table.html](https://docs.aws.amazon.com/quick/latest/userguide/pivot-table.html)

---

Use pivot tables to show measure values for the intersection of two dimensions.

Heat maps and pivot tables display data in a similar tabular fashion. Use a heat map if you want to identify trends and outliers, because the use of color makes these easier to spot. Use a pivot table if you want to analyze data on the visual.

To create a pivot table, choose at least one field of any data type, and choose the pivot table icon. Amazon Quick creates the table and populates the cell values with the count of the column value for the intersecting row value. Typically, you choose a measure and two dimensions measurable by that measure.

Pivot tables support scroll down and right. You can add up to 20 fields as rows and 20 fields as columns. Up to 500,000 records are supported.

Using a pivot table, you can do the following:

- 
				Specify multiple measures to populate the cell values of the table, so that you can see a range of data 
- 
				Cluster pivot table columns and rows to show values for subcategories grouped by related dimension 
- 
				Sort values in pivot table rows or columns 
- 
				Apply statistical functions 
- 
				Add totals and subtotals to rows and columns 
- 
				Use infinite scroll 
- 
				Transpose fields used by rows and columns 
- 
				Create custom total aggregations 

To easily transpose the fields used by the rows and columns of the pivot table, choose
			the orientation icon (
				 
					![Icon showing an arrow pointing from a circle to a square, indicating a share or export action.](/images/quick/latest/userguide/images/pivot-orientation.png) ) near the top right of the visual. To see options for showing and
			hiding totals and subtotals, formatting the visual, or exporting data to a CSV file,
			choose the Menu items icon at top right.

				 
				 
			) near the top right of the visual. To see options for showing and
			hiding totals and subtotals, formatting the visual, or exporting data to a CSV file,
			choose the Menu items icon at top right. 

As with all visual types, you can add and remove fields. You can also change the field
			associated with a visual element, change field aggregation, and change date field
			granularity. In addition, you can focus on or exclude rows or columns. For more
			information about how to make these changes to a pivot table, see [Changing fields used by a visual in Amazon Quick](./changing-visual-fields.html). 

For information on formatting pivot tables, see [Formatting in Amazon Quick](./formatting-a-visual.html).

For information on custom total aggregations for pivot tables, see [Custom total values](./tables-pivot-tables-custom-totals.html).

###### Topics

## Pivot table features

			Pivot tables don't display a legend.

To understand the features supported by pivot tables, use the following table.

| Feature | Supported? | Comments | For more information | 
|---|---|---|---|
| Changing the legend display | No | [Legends on visual types in Quick](./customizing-visual-legend.html) | |
| Changing the title display | Yes | [Titles and subtitles on visual types in Quick](./customizing-a-visual-title.html) | |
| Changing the axis range | Not applicable | [Range and scale on visual types in Quick](./changing-visual-scale-axis-range.html) | |
| Changing the visual colors | No | [Colors in visual types in Quick](./changing-visual-colors.html) | |
| Focusing on or excluding elements | Yes, with exceptions | You can focus on or exclude any column or row, except when you are using a date field as one of the dimensions. In that case, you can only focus on the column or row that uses the date dimension, not exclude it. | |
| Sorting | Yes | You can sort fields in the RowsorColumnsfield wells alphabetically or by a
								metric in ascending or descending order. | |
| Performing field aggregation | Yes | You must apply aggregation to the field or fields you choose for the value. You can't apply aggregation to the fields that you choose for the rows or columns. If you choose to create a multi-measure pivot table, you can apply different types of aggregation to the different measures. For example, you can show the sum of the sales amount and the maximum discount amount. | [Changing field aggregation](./changing-field-aggregation.html) | 
| Adding drill-downs | No | [Adding drill-downs to visual data in Quick Sight](./adding-drill-downs.html) | |
| Showing and hiding totals and subtotals | Yes | You can show or hide totals and subtotals for rows and columns. Metrics automatically roll up to show subtotals when you collapse a row or column. If you use a table calculation, use aggregates to display roll-ups. | |
| Exporting or copying data | Yes | You can export all of the data to a CSV file. You can select and copy the content of the cells. | [Exporting data from visuals](./exporting-data.html) | 
| Conditional formatting | Yes | You can add conditional formatting for values, subtotals and totals. | [Conditional formatting on visual types in Quick](./conditional-formatting-for-visuals.html) |
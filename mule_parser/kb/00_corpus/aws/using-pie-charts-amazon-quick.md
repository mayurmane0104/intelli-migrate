# Using pie charts - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/pie-chart.html](https://docs.aws.amazon.com/quick/latest/userguide/pie-chart.html)

---

Use pie charts to compare values for items in a dimension. The best use for this type of chart is to show a percentage of a total amount.

Each wedge in a pie chart represents one item in the dimension. Wedge size represents the proportion of the value for the selected measure that the item represents compared to the whole for the dimension. Pie charts are best when precision isn't important and there are few items in the dimension.

To create a donut chart, use one dimension in the **Group/Color**
			field well. With only one field, the chart displays the division of values by row count.
			To display the division of dimension values by a metric value, you can add a metric
			field to the **Value** field well. 

Pie charts show up to 20 data points for group or color. For more information about
			how Amazon Quick handles data that falls outside display limits, see [Display limits](./working-with-visual-types.html#display-limits).

## Pie chart features

			To understand the features supported by pie charts, use the following table.

| Feature | Supported? | Comments | For more information | 
|---|---|---|---|
| Changing the legend display | Yes | [Legends on visual types in Quick](./customizing-visual-legend.html) | |
| Changing the title display | Yes | [Titles and subtitles on visual types in Quick](./customizing-a-visual-title.html) | |
| Changing the axis range | Not applicable | [Range and scale on visual types in Quick](./changing-visual-scale-axis-range.html) | |
| Showing or hiding axis labels. | Yes | [Axes and grid lines on visual types in Quick](./showing-hiding-axis-grid-tick.html) | |
| Changing the visual colors | Yes | [Colors in visual types in Quick](./changing-visual-colors.html) | |
| Focusing on or excluding elements | Yes, with exceptions | You can focus on or exclude a wedge in a pie chart, except when you are using a date field as a dimension. In that case, you can only focus on a wedge, not exclude it. | |
| Sorting | Yes | You can sort on the field that you choose for the value or the group or color. | [Sorting visual data in Amazon Quick](./sorting-visual-data.html) | 
| Performing field aggregation | Yes | You must apply aggregation to the field that you choose for the value, and can't apply aggregation to the field that you choose for group or color. | [Changing field aggregation](./changing-field-aggregation.html) | 
| Adding drill-downs | Yes | You can add drill-down levels to the Group/Colorfield well. | [Adding drill-downs to visual data in Quick Sight](./adding-drill-downs.html) | 

## Creating a pie chart

			Use the following procedure to create a pie chart.

###### To create a pie chart

- 
					On the analysis page, choose **Visualize**on the tool bar.
- 
					Choose **Add**on the application bar, and then choose**Add visual**.
- 
					On the **Visual types**pane, choose the pie chart icon.
- 
					From the **Fields list**pane, drag the fields that you want to use to the appropriate field wells. Typically, you want to use dimension or measure fields as indicated by the target field well. If you choose to use a dimension field as a measure, the**Count**aggregate function is automatically applied to it to create a numeric value.To create a pie chart, drag a dimension to the **Group/Color**field well. Optionally, drag a measure to the**Value**field well.
- 
					(Optional) Add drill-down layers by dragging one or more additional fields to the **Group/Color**field well. For more information about adding drill-downs, see[Adding drill-downs to visual data in Quick Sight](./adding-drill-downs.html).
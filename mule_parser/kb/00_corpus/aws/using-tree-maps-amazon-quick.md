# Using tree maps - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/tree-map.html](https://docs.aws.amazon.com/quick/latest/userguide/tree-map.html)

---

To visualize one or two measures for a dimension, use tree maps.

Each rectangle on the tree map represents one item in the dimension. Rectangle size represents the proportion of the value for the selected measure that the item represents compared to the whole for the dimension. You can optionally use rectangle color to represent another measure for the item. Rectangle color represents where the value for the item falls in the range for the measure, with darker colors indicating higher values and lighter colors indicating lower ones.

Tree maps show up to 100 data points for the **Group by** field. For
			more information about how Amazon Quick handles data that falls outside display limits,
			see [Display limits](./working-with-visual-types.html#display-limits).

## Tree map features

			To understand the features supported by tree maps, use the following table.

| Feature | Supported? | Comments | For more information | 
|---|---|---|---|
| Changing the legend display | Yes | [Legends on visual types in Quick](./customizing-visual-legend.html) | |
| Changing the title display | Yes | [Titles and subtitles on visual types in Quick](./customizing-a-visual-title.html) | |
| Changing the axis range | Not applicable | [Range and scale on visual types in Quick](./changing-visual-scale-axis-range.html) | |
| Changing the visual colors | No | [Colors in visual types in Quick](./changing-visual-colors.html) | |
| Focusing on or excluding elements | Yes, with exceptions | You can focus on or exclude a rectangle from a tree map, except when you are using a date field as the dimension. In that case, you can only focus on a rectangle, not exclude it. | |
| Sorting | No | Default sorting is in descending order by the measure in the Sizecolumn. | [Sorting visual data in Amazon Quick](./sorting-visual-data.html) | 
| Performing field aggregation | Yes | You must apply aggregation to the fields you choose for size and color, and can't apply aggregation to the field that you choose to group by. | [Changing field aggregation](./changing-field-aggregation.html) | 
| Adding drill-downs | Yes | You can add drill-down levels to the Group
									byfield well. | [Adding drill-downs to visual data in Quick Sight](./adding-drill-downs.html) | 

## Creating a tree map

			Use the following procedure to create a tree map.

###### To create a tree map

- 
					On the analysis page, choose **Visualize**on the tool bar.
- 
					Choose **Add**on the application bar, and then choose**Add visual**.
- 
					On the **Visual types**pane, choose the tree map icon.
- 
					From the **Fields list**pane, drag the fields that you want to use to the appropriate field wells. Typically, you want to use dimension or measure fields as indicated by the target field well. If you choose to use a dimension field as a measure, the**Count**aggregate function is automatically applied to it to create a numeric value.To create a tree map, drag a measure to the **Size**field well and a dimension to the**Group by**field well. Optionally, drag another measure to the**Color**field well.
- 
					(Optional) Add drill-down layers by dragging one or more additional fields to the **Group by**field well. For more information about adding drill-downs, see[Adding drill-downs to visual data in Quick Sight](./adding-drill-downs.html).
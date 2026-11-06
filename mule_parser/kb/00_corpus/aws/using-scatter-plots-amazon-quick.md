# Using scatter plots - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/scatter-plot.html](https://docs.aws.amazon.com/quick/latest/userguide/scatter-plot.html)

---

Use scatter plots to visualize two or three measures across two dimensions.

Each bubble on the scatter plot represents one or two dimension values. The X and Y axes represent two different measures that apply to the dimension. A bubble appears on the chart at the point where the values for the two measures for an item in the dimension intersect. Optionally, you can also use bubble size to represent an additional measure.

Scatter plots show up to 2500 datapoints in aggregated and unaggregated scenarios
			regardless of whether a color or label dimension is used in the visual. Due to the order
			of limit operations, there may be cases where fewer datapoints for a dataset are shown.
			For more information about how Amazon Quick handles data that falls outside display
			limits, see [Display limits](./working-with-visual-types.html#display-limits).

## Scatter plot features

			To understand the features supported by scatter plots, use the following table.

| Feature | Supported? | Comments | For more information | 
|---|---|---|---|
| Changing the legend display | Yes, with exceptions | Scatter plots display a legend if you have the Group/Colorfield well populated. | [Legends on visual types in Quick](./customizing-visual-legend.html) | 
| Changing the title display | Yes | [Titles and subtitles on visual types in Quick](./customizing-a-visual-title.html) | |
| Changing the axis range | Yes | You can set the range for both the X and Y axes. | [Range and scale on visual types in Quick](./changing-visual-scale-axis-range.html) | 
| Showing or hiding axis lines, grid lines, axis labels, and axis sort icons | Yes | [Axes and grid lines on visual types in Quick](./showing-hiding-axis-grid-tick.html) | |
| Changing the visual colors | Yes | [Colors in visual types in Quick](./changing-visual-colors.html) | |
| Focusing on or excluding elements | Yes, with exceptions | You can focus on or exclude a bubble in a scatter plot, except when you are using a date field as a dimension. In that case, you can only focus on a bubble, not exclude it. | |
| Sorting | No | [Sorting visual data in Amazon Quick](./sorting-visual-data.html) | |
| Performing field aggregation | Yes | You must apply aggregation to the fields you choose for the X axis, Y axis, and size, and can't apply aggregation to the field that you choose for the group or color. | [Changing field aggregation](./changing-field-aggregation.html) | 
| Displaying unaggregated fields | Yes | On the field context menu, choose Noneto
								display unaggregated X and Y axis values. If your scatter plot shows
								unaggregated fields, you can't apply aggregations to the field
								that is in the color or label field well. Mixed aggregation is not
								supported for scatter plots. | |
| Adding drill-downs | Yes | You can add drill-down levels to the Group/Colorfield well. | [Adding drill-downs to visual data in Quick Sight](./adding-drill-downs.html) | 

## Creating a scatter plot

			Use the following procedure to create a scatter plot.

###### To create a scatter plot

- 
					On the analysis page, choose **Visualize**on the tool bar.
- 
					Choose **Add**on the application bar, and then choose**Add visual**.
- 
					On the **Visual types**pane, choose the scatter plot icon.
- 
					From the **Fields list**pane, drag the fields that you want to use to the appropriate field wells. Typically, you want to use dimension or measure fields as indicated by the target field well. If you choose to use a dimension field as a measure, the**Count**aggregate function is automatically applied to it to create a numeric value.To create a scatter plot, drag a measure to the **X axis**field well, a measure to the**Y axis**field well, and a dimension to the**Color**or**Label**field well. To represent another measure with bubble size, drag that measure to the**Size**field well.
- 
					(Optional) Add drill-down layers by dragging one or more additional fields to the **Color**field well. For more information about adding drill-downs, see[Adding drill-downs to visual data in Quick Sight](./adding-drill-downs.html).

## Scatter plot use cases

			You can choose to plot unaggregated values even if you are using a field on Color
				by using the aggregate option **none** on the field menu, which
				also contains aggregation options like **sum**,
					**min**, and **max**. If one value is set to
				be aggregated, the other value will be automatically set as aggregated. The same
				applies to unaggregated scenarios. Mixed aggregation scenarios are not supported,
				meaning that one value cannot be set as aggregated while the other is unaggregated.
				Note that the unaggregated scenario, which is the **none** option, is supported only for numerical values, while
				categorical values, such as dates or dimensions, will display only aggregate values,
				such as **count** and **count distinct**.

Using the **none** option, you can choose to set both X and Y
				values to either aggregated or unaggregated from the **X axis** and
					**Y axis** field menus. This will define whether or not values
				will be aggregated by dimensions in the **Color** and
					**Label** field wells. To get started, add the required fields
				and choose the appropriate aggregation based on your use case,as shown in the
				following sections. 

### Unaggregated use cases

- 
						Unaggregated X and Y values with Color ![unaggregated-color](/images/quick/latest/userguide/images/unaggregated-color.png)  
- 
						Unaggregated X and Y values with Label ![unaggregated-label](/images/quick/latest/userguide/images/unaggregated-label.png)  
- 
						Unaggregated X and Y values with Color and Label ![unaggregated-color-label](/images/quick/latest/userguide/images/unaggregated-color-label.png)  

### Aggregated use cases

- 
						Aggregated X and Y values with Color ![aaggregated-color](/images/quick/latest/userguide/images/aggregated-color.png)  
- 
						Aggregated X and Y values with Label ![aggregated-label](/images/quick/latest/userguide/images/aggregated-label.png)  
- 
						Aggregated X and Y values with Color and Label ![aggregated-color-label](/images/quick/latest/userguide/images/aggregated-color-label.png)
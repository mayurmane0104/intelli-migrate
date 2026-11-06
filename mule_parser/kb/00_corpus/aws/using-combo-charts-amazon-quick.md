# Using combo charts - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/combo-charts.html](https://docs.aws.amazon.com/quick/latest/userguide/combo-charts.html)

---

Using a combo chart, you can create one visualization that shows two different types of data, for example trends and categories. Combo charts are also known as line and column (bar) charts, because they combine a line chart with a bar chart. Bar charts are useful for comparing categories. Both bar charts and line charts are useful for displaying changes over time, although bar charts should show a greater difference between changes.

Amazon Quick supports the following types of combo charts:

- 
				**Clustered bar combo charts**– display sets of single-color bars where each set represents a parent dimension and each bar represents a child dimension. Use this chart to make it easy to determine values for each bar.
- 
				**Stacked bar combo charts**– display multi-color bars where each bar represents a parent dimension and each color represents a child dimension. Use this chart to make it easy to see relationships between child dimensions within a parent dimension. This chart shows the total value for the parent dimension and how each child adds to the total value. To determine the value for each child dimension, the chart reader must compare the size of the color section to the data labels for that axis.

Both types of combo chart require only one dimension on the **X
				axis**, but are usually more effective when also displaying at least one
			measure under **Lines**. 

Use a combo chart only if you want to show a relationship between the bars and the lines. A good rule of thumb is that if you need to explain how the two chart types relate, you should probably use two separate charts instead.

Because each chart works differently, it can be helpful to understand the following points before you begin:

- 
				The data points in each series render on different scales. Combo charts use a scale based on the maximum value for the selected measure. 
- 
				The distance between the numbers on the axis won't match between the lines and bars, even if you select the same scale for each chart type. 
- 
				For clarity, try to use different units for the measure in each data series. 

The combo chart is like using two different types of visualization at the same time. Make sure that the data in the bars (or columns) directly relates to the data in the line or lines. This relationship is not technically enforced by the tool, so it's essential that you determine this relationship yourself. Without some relation between the lines and bars, the visual loses meaning.

You can use the combo chart visual type to create a single-measure or single-line chart. A single-measure combo chart shows one measure for one dimension.

To create a multi-measure chart, you can choose to add multiple lines, or multiple bars. A multi-measure bar chart shows two or more measures for one dimension. You can group the bars in clusters, or stack them.

For the bars, use a dimension for the axis and a measure for the value. The dimension is typically a text field that is related to the measure in some way and can be used to segment it to see more detailed information. Each bar in the chart represents a measure value for an item in the dimension you chose.

Bars and lines show up to 2,500 data points on the axis for visuals that don't
			use group or color. For visuals that do use group or color, bars show up to 50 data
			points on the axis and up to 50 data points for group or color, while lines show 200
			data points on the axis and up to 25 data points for group or color. For more
			information about how Amazon Quick handles data that falls outside display limits, see
				[Display limits](./working-with-visual-types.html#display-limits).

## Combo chart features

			To understand the features supported by combo charts, use the following table.

| Feature | Supported? | Comments | For more information | 
|---|---|---|---|
| Changing the legend display | Yes, with exceptions | Multi-measure combo charts display a legend, and single-measure combo charts don't. | [Legends on visual types in Quick](./customizing-visual-legend.html) | 
| Changing the title display | Yes | [Titles and subtitles on visual types in Quick](./customizing-a-visual-title.html) | |
| Changing the axis range | Yes | You can set the range for the axis. | [Range and scale on visual types in Quick](./changing-visual-scale-axis-range.html) | 
| Showing or hiding axis lines, grid lines, axis labels, and axis sort icons | Yes | [Axes and grid lines on visual types in Quick](./showing-hiding-axis-grid-tick.html) | |
| Changing the visual colors | Yes | [Colors in visual types in Quick](./changing-visual-colors.html) | |
| Focusing on or excluding elements | Yes, with exceptions | You can focus on or exclude any bar on the chart, except when you are using a date field as the dimension for the axis. In that case, you can only focus on a bar, not exclude it. | |
| Sorting | Yes | You can sort on the fields you choose for the axis and the values. | [Sorting visual data in Amazon Quick](./sorting-visual-data.html) | 
| Performing field aggregation | Yes | You must apply aggregation to the field or fields you choose for the value. You can't apply aggregation to the fields you choose for the axis or group/color. | [Changing field aggregation](./changing-field-aggregation.html) | 
| Adding drill-downs | Yes | You can add drill-down levels to the axis and Group/Colorfield wells. | [Adding drill-downs to visual data in Quick Sight](./adding-drill-downs.html) | 
| Synchronizing y-axis | Yes | Synchronize the y-axes for both bars and lines into a single axis. | [Range and scale on visual types in Quick](./changing-visual-scale-axis-range.html) | 

## Creating a combo chart

			Use the following procedure to create a combo chart.

###### To create a combo chart

- 
					On the analysis page, choose **Visualize**on the tool bar.
- 
					Choose **Add**on the application bar, and then choose**Add visual**.
- 
					On the **Visual types**pane, choose one of the combo chart icons.
- 
					From the **Fields list**pane, drag the fields that you want to use to the appropriate field wells. Typically, you want to use dimension or measure fields as indicated by the target field well. If you choose to use a dimension field as a measure, the**Count**aggregate function is automatically applied to it to create a numeric value. You can create combo charts as follows:- 
							Choose a dimension for the **X axis**.
- 
							To create a single-measure combo chart, choose one measure for either **Bars**or**Lines**.
- 
							To create a multi-measure combo chart, choose two or more measures for the **Bars**or**Lines**field well.
- 
							Optionally, add a dimension to the **Group/Color**field well. If you have a field in**Group/Color**, you can't have more than one field under**Bars**.
 ![Bar chart showing website metrics by event type, with empty having highest visits and declining trend line overlay.](/images/quick/latest/userguide/images/combo-chart-example2-clustered.png)  
- 
							
- 
					(Optional) Add drill-down layers by dragging one or more additional fields to the **X axis**or**Group/Color**field wells. For more information about adding drill-downs, see[Adding drill-downs to visual data in Quick Sight](./adding-drill-downs.html).
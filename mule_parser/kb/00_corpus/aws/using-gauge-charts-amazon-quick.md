# Using gauge charts - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/gauge-chart.html](https://docs.aws.amazon.com/quick/latest/userguide/gauge-chart.html)

---

Use gauge charts to compare values for items in a measure. You can compare them to another measure or to a custom amount.

A gauge chart is similar to a nondigital gauge, for example a gas gauge in an automobile. It displays how much there is of the thing you are measuring. In a gauge chart, this measurement can exist alone or in relation to another measurement. Each color section in a gauge chart represents one value. In the following example, we are comparing actual sales to the sales goal, and the gauge shows that we must sell an additional 33.27% to meet the goal.

To learn how to use gauge charts in Amazon Quick, you can watch this video:

To create a gauge chart, you need to use at least one measure. Put the measure in the
				**Value** field well. If you want to compare two measures, put the
			additional measure in the **Target value** field well. If you want to
			compare a single measure to a target value that isn't in your dataset, you can use
			a calculated field that contains a fixed value. 

You can choose a variety of formatting options for the gauge chart, including the
			following settings in **Format visual**.

- 
				**Value displayed**– Hide value, display actual value, or display a comparison of two values
- 
				**Comparison method**– Compare values as a percent, the actual difference between values, or difference as a percent
- 
				**Axis style**–- 
						**Show axis label**– Show or hide the axis label
- 
						**Range**– The numeric minimum and maximum range to display in the gauge chart
- 
						**Reserve padding (%)**– Added to the top of the range (target, actual value, or max)
 
- 
						
- 
				**Arc style**– Degrees the arc displays (180° to 360°)
- 
				**Thickness**– Thickness of the arc (small, medial, or large)

## Gauge chart features

			To understand the features supported by gauge charts, use the following table.

| Feature | Supported? | Comments | For more information | 
|---|---|---|---|
| Changing the legend display | Yes | [Legends on visual types in Quick](./customizing-visual-legend.html) | |
| Changing the title display | Yes | [Titles and subtitles on visual types in Quick](./customizing-a-visual-title.html) | |
| Formatting gauge | Yes | You can customize the value displayed, the comparison method, the axis style, the arc style, and the thickness of the gauge. | |
| Changing the axis range | No | ||
| Changing the visual colors | Yes | The foreground color the filled area; it represents the Value. The background color the unfilled
								area; it represents theTarget valueif one is
								selected. | [Colors in visual types in Quick](./changing-visual-colors.html) | 
| Focusing on or excluding elements | No | ||
| Sorting | No | [Sorting visual data in Amazon Quick](./sorting-visual-data.html) | |
| Performing field aggregation | Yes | [Changing field aggregation](./changing-field-aggregation.html) | |
| Adding drill-downs | No | 

## Creating a gauge chart

			Use the following procedure to create a gauge chart.

###### To create a gauge chart

- 
					On the analysis page, choose **Visualize**on the tool bar.
- 
					Choose **Add**on the application bar, and then choose**Add visual**.
- 
					On the **Visual types**pane, choose the gauge chart icon.
- 
					From the **Fields list**pane, drag the fields that you want to use to the appropriate field wells. To create a gauge chart, drag a measure to the**Value**field well. To add a comparison value, drag a different measure to the**Target value**field well.
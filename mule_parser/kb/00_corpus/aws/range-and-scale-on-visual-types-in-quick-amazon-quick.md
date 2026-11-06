# Range and scale on visual types in Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/changing-visual-scale-axis-range.html](https://docs.aws.amazon.com/quick/latest/userguide/changing-visual-scale-axis-range.html)

---

To change the scale of the values shown on the visual, you can use the
				**Properties** pane to set the range for one or both axes of the
			visual. This option is available for the value axes on bar charts, combo charts, line
			charts, and scatter plots. 

By default, the axis range starts at 0 and ends with the highest value for the measure being displayed. For the group-by axis, you can use the data zoom tool on the visual to dynamically adjust the scale.

###### To set the axis range for a visual

- 
				On the analysis page, choose the visual that you want to format. 
- 
				Choose the control menu at the upper-right corner of the visual, and then choose the cog icon. 
- 
				On the **Properties**pane, choose**X-Axis**or**Y-Axis**, depending on what type of visual you are customizing. This is the**X-Axis**section for horizontal bar charts, the**Y-Axis**section for vertical bar charts and line charts, and both axes are available for scatter plots. On combo charts, use**Bars**and**Lines**instead.
- 
				Enter a new name in the box to rename the axis. To revert to the default name, delete your entry. 
- 
				Set the range for the axis by choosing one of the following options: - 
						Choose **Auto (starting at 0)**to have the range start at 0 and end around the highest value for the measure being displayed.
- 
						Choose **Auto (based on data range)**to have the range start at the lowest value for the measure being displayed and end around the highest value for the measure being displayed.
- 
						Choose **Custom**to have the range start and end at values that you specify.If you choose **Custom**, enter the start and end values in the fields in that section. Typically, you use integers for the range values. For stacked 100 percent bar charts, use a decimal value to indicate the percentage that you want. For example, if you want the range to be 0–30 percent instead of 0–100 percent, enter 0 for the start value and .3 for the end value.
 
- 
						
- 
				For **Scale**, the default is linear scale. To show logarithmic scale, also called log scale, enable the logarithmic option. Quick chooses the axis labels to display based on the range of values in that axis.- 
						On a linear scale, the axis labels are evenly spaced to show the arithmetical difference between them. The labels display the numbers in sets like {1000, 2000, 3000…} or {0, 50 million, 100 million…}, but not {10 thousand, 1 million, 1 billion…}. Use a *linear scale*for the following cases:- 
								All the numbers that display on the chart are in the same order of magnitude. 
- 
								You want the axis labels to be evenly spaced. 
- 
								The axis values have a similar number of digits, for example 100, 200, 300, and so on. 
- 
								The rate of change between numbers is relatively slow and steady—in other words, your trend line never approaches becoming vertical. 
 Examples: - 
								Profits in different regions of the same country 
- 
								Costs incurred for manufacture of an item 
 
- 
								
- 
						On a *logarithmic scale*, the axis values are spaced to show the orders of magnitude as a way of comparing them. The log scale is often used to display very large ranges of values or percentages, or to show exponential growth.Use logarithmic scale for the following cases: - 
								The numbers that display on the chart aren’t in the same order of magnitude. 
- 
								You want the axis labels to be flexibly spaced to reflect the wide range of values in that axis. This might mean that the axis values have a different number of digits, for example 10, 100, 1000, and so on. It might also mean that the axis labels are unevenly spaced. 
- 
								The rate of change between numbers is growing exponentially or is too large to display in a meaningful way. 
- 
								The customer of your chart understands how to interpret data on a log scale. 
- 
								The chart displays values that growing faster and faster. Moving given distance on the scale means the number has been multiplied by another number. 
 Examples: - 
								High yield stock prices over a long range of time 
- 
								Growth of pandemic infection rates 
 
- 
								
 
- 
						
- 
				To customize the number of values to show on the axis labels, enter in an integer between 1 and 50. 
- 
				For combo charts, choose **Single Y Axis**to synchronize the Y-axes for both bars and lines into a single axis.
- 
				Close the **Properties**pane by choosing the**X**icon in the upper-right corner of the pane.
# Using word clouds - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/word-cloud.html](https://docs.aws.amazon.com/quick/latest/userguide/word-cloud.html)

---

As an engaging way to display how often a word is used in relation to other words in a dataset, use word clouds. The best use for this type of visual is to show word or phrase frequency. It can also make a fun addition to show trending items or actions. You can use a fixed dataset for creative purposes. For example, you might make one of team goals, motivational phrases, various translations of a specific word, or anything else that you want to draw attention to.

Each word in a word cloud represents one or more values in a dimension. The size of the word represents the frequency of a value's occurrence in a selected dimension, in proportion to the occurrences of other values in the same dimension. Word clouds are best when precision isn't important and there aren't a large number of distinct values.

The following screenshot shows an example of a word cloud.

![Word cloud showing top 100 lead names with various enterprise and startup identifiers.](/images/quick/latest/userguide/images/word-cloud.png) 

			 
			 
		To create a word cloud, use one dimension in the **Group by** field
			well. Optionally, you can add a metric to the **Size** field
			well.

Word clouds usually look better with 20–100 words or phrases, but the format
			settings offer a wide range of flexibility. If you choose too many words, they can
			become too small to be legible, depending on the size of your display. By default, word
			clouds display 100 distinct words. To show more, change the format setting for
				**Number of words**. 

Word clouds are limited to 500 unique values for **Group by**. To
			avoid displaying the word `Other`, format the visual to hide the
				**Other** category. For more information about how Amazon Quick
			handles data that falls outside display limits, see [Display limits](./working-with-visual-types.html#display-limits).

## Word cloud features

			To understand the features supported by word clouds, see the following table.

| Feature | Supported? | Comments | For more information | 
|---|---|---|---|
| Changing the legend display | No | [Legends on visual types in Quick](./customizing-visual-legend.html) | |
| Changing the title display | Yes | [Titles and subtitles on visual types in Quick](./customizing-a-visual-title.html) | |
| Changing the axis range | Not applicable | [Range and scale on visual types in Quick](./changing-visual-scale-axis-range.html) | |
| Changing the visual colors | Yes | To change the color, choose a word and then choose a color. | [Colors in visual types in Quick](./changing-visual-colors.html) | 
| Focusing on or excluding elements | Yes | ||
| Sorting | Yes | [Sorting visual data in Amazon Quick](./sorting-visual-data.html) | |
| Performing field aggregation | Yes | You can't apply aggregation to the field that you choose for Group by. You must apply an aggregation to
								the field that you choose forSize. | [Changing field aggregation](./changing-field-aggregation.html) | 
| Adding drill-downs | Yes | You can add drill-down levels to the Group
									byfield well. | [Adding drill-downs to visual data in Quick Sight](./adding-drill-downs.html) | 
| Using format options | Yes | You can choose to allow vertical words, emphasize scale, use a
								fluid layout, use lowercase, and set the amount of padding between
								words. You can set the maximum string length for the word cloud
								(default is 40). You can also choose the number of words for the Group byfield (default is 100; maximum is
								500). | [Formatting in Amazon Quick](./formatting-a-visual.html) | 
| Showing totals | No | [Formatting in Amazon Quick](./formatting-a-visual.html) | 

## Creating a word cloud

			Use the following procedure to create a word cloud.

###### To create a word cloud

- 
					On the analysis page, choose **Visualize**on the tool bar.
- 
					Choose **Add**on the application bar, and then choose**Add visual**.
- 
					On the **Visual types**pane, choose the word cloud icon.
- 
					From the **Fields list**pane, drag the fields that you want to use to the appropriate field wells. Typically, you want to use dimension or measure fields as indicated by the target field well. If you choose to use a dimension field as a measure, the**Count**aggregate function is applied by default.To create a word cloud, add a dimension to the **Group by**field well. Optionally, add a measure to the**Size**field well.
- 
					(Optional) Add drill-down layers by dragging one or more additional fields to the **Group by**field well. For more information about adding drill-downs, see[Adding drill-downs to visual data in Quick Sight](./adding-drill-downs.html).
# Visual types in Amazon Quick Sight - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/working-with-visual-types.html](https://docs.aws.amazon.com/quick/latest/userguide/working-with-visual-types.html)

---

Amazon Quick Sight offers a range of visual types that you can use to display your data. Use the topics in this section to learn more about the capabilities of each visual type.

###### Topics

## Measures and dimensions

		We use the term *measure* to refer to numeric values that you use
			for measurement, comparison, and aggregation in visuals. A measure can be either a
			numeric field, like product cost, or a numeric aggregate on a field of any data type,
			like count of transaction IDs.

We use the term *dimension* or *category* to
			refer to text or date fields that can be items, like products, or attributes that are
			related to measures and can be used to partition them. Examples are sales date for sales
			figures or product manufacturer for customer satisfaction numbers. Amazon Quick Sight automatically
			identifies a field as a measure or a dimension based on its data type. 

Numeric fields can act as dimensions, for example ZIP codes and most ID numbers. It's helpful to give such fields a string data type during data preparation. This way, Amazon Quick Sight understands that they are to be treated as dimensions and are not useful for performing mathematical calculations.

You can change whether a field is displayed as a dimension or measure on an
			analysis-by-analysis basis instead. For more information, see [Fields as dimensions and measures](./creating-a-visual.html#dimensions-and-measures).

## Display limits

		All visual types limit the number of data points they display, so that the visual
			elements (like lines, bars, or bubbles) are still easy to view and analyze. The visual
			selects the first *n* number of rows for display up to the limit for
			that visual type. The selection is either according to sort order, if one has been
			applied, or in default order otherwise. 

The number of data points supported varies by visual type. To learn more about display limits for a particular visual type, see the topic for that type.

The visual title identifies the number of data points displayed if you have reached
			the display limit for that visual type. If you have a large dataset and want to avoid
			running into the visual display limit, use one or more filters to reduce the amount of
			data displayed. For more information about using filters with visuals, see [Filtering data in Amazon Quick Sight](./adding-a-filter.html).

For dashboards and analyses, Amazon Quick Sight supports the following:

- 
				50 datasets per dashboard 
- 
				20 sheets per dashboard 
- 
				30 visualization objects per sheet 

###### Note

Amazon Quick Sight supports over 30 different *visual types* (categories of
				charts and visualizations such as bar charts, pie charts, and line charts). Each analysis
				sheet can contain up to 30 *visual instances* (individual chart
				objects) of any combination of types.

You can also choose to limit how many data points you want to display in your visual,
			before they are added to the **other** category. This category contains
			the aggregated data for all the data beyond the cutoff limit for the visual type you are
			using—either the one you impose, or the one based on display limits. You can use
			the on-visual menu to choose whether to display the **other** category.
			The **other** category doesn't show on scatter plots, heat maps,
			maps, tables (tabular reports), or key performance indicators (KPIs). It also
			doesn't show on line charts when the x-axis is a date. Drilling down into the
				**other** category is not supported. 

## Hiding or displaying the other category

		Use the following procedure to hide or display the "other" category.

###### To hide or display the "other" category

- 
				On the analysis page, choose the visual that you want to modify. 
- 
				Choose the on-visual menu at the upper-right corner of the visual, and then choose **Hide "other" category**or**Show "other" category**, as appropriate.

## Customizing the number of data points to display

		You can choose the number of data points to display on the main axis of some visuals. After this number is displayed in the chart, any additional data points are included in the "other" category. For example, if you choose to include 10 data points out of 200, 10 display in the chart and 190 become part of the "other" category.

To find this setting, choose the **v**-shaped on-visual menu, then
			choose **Format visual**. You can use the following table to determine
			which field well contains the data point setting and what number of data points the
			visual type displays by default. 

| Visual type | Where to find the data point setting | Default number of data points | 
|---|---|---|
| Bar chart, horizontal | 
 | 10,000 | 
| Bar chart, vertical | 
 | 10,000 | 
| Combo chart | 
 | 2,500 | 
| Heat map | 
 
 | 100 | 
| Line chart | 
 | 10,000 | 
| Pie chart | 
 | 20 | 
| Tree map | 
 | 100 |
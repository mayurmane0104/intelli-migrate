# Adding sparklines to tables in Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/format-sparklines.html](https://docs.aws.amazon.com/quick/latest/userguide/format-sparklines.html)

---

Sparklines are small inline charts that display trends directly within table cells, helping readers quickly identify patterns and seasonality without leaving the table view. Use sparklines when you need compact trend visualization alongside your tabular data.

###### To apply sparklines to a table

- 
				On the analysis page, choose the table visual that you want to format. 
- 
				On the menu in the upper-right corner of the visual, select the **Format visual**icon. The**Format visual**pane opens.
- 
				In the **Properties**pane, open the**Visuals**dropdown list and choose**APPLY SPARKLINES**.
- 
				In the sparklines editing pane, configure the data settings: - 
						For **Value column**, choose the measure field that you want the sparkline to represent. Fields already used by another sparkline or data bar are not available.
- 
						For **X-axis field**, choose the dimension field to plot along the horizontal axis. The X-axis field must not be the same as a field in the**Group by**field well. You can also configure the sort direction and time granularity (for date/time fields) of the X-axis field.
 
- 
						
- 
				(Optional) Expand the **Presentation**section to customize the sparkline appearance. See[Sparkline options](#format-sparklines-options)for details.
- 
				(Optional) Configure marker visibility. All markers are hidden by default. You can choose to show: - 
						**All points**– Show a marker on every data point.
- 
						**Max value**– Show a marker on the highest value.
- 
						**Min value**– Show a marker on the lowest value.
 
- 
						
- 
				Choose **Apply**.

The sparkline is named after the value field it represents (for example,
			"Profit"). Sparklines appear in the **Visuals** pane in the
			order they are created.

## Sparkline options

			The following table describes the sparkline presentation options.

| Setting | Options | Default | Description | 
|---|---|---|---|
| Y-axis behavior | Shared, Independent | Shared | Shared uses the same Y-axis scale across all rows for easy comparison. Independent scales each row separately to highlight individual trend shapes. | 
| Visual type | Line, Area line | Line | Area line adds a shaded area beneath the line. | 
| Line color | Color picker | Theme color | Custom color for the sparkline line. | 
| Line interpolation | Linear, Smooth, Stepped | Linear | Controls how points are connected. | 

## Editing and removing sparklines

			To edit a sparkline, open the **Visuals** dropdown in the
					**Format visual** pane and choose the edit icon next to the
				sparkline you want to modify. Update the settings and choose
					**Apply**.

To remove a sparkline, open the edit pane for the sparkline and choose
					**Delete**.

## Automatic removal

			Quick automatically removes sparklines when field changes make them invalid:

- 
					All **Group by**fields are removed – all sparklines are removed.
- 
					A sparkline's value column is removed from the **Values**field well – that sparkline is removed.
- 
					A sparkline's X-axis field is added to the **Group by**field well – that sparkline is removed.

A notification appears when a sparkline is automatically removed.

## Sparkline limitations

			Consider the following when working with sparklines:

- 
					**Maximum sparklines per table**– Up to 3 sparkline columns per table visual
- 
					**Maximum data points**– Up to 52 data points per sparkline. If your data exceeds this limit, Quick displays the last 52 data points according to your X-axis sort order.
- 
					**Field requirements**– At least one field in the**Group by**field well and one field in the**Values**field well
- 
					**X-axis constraint**– The X-axis field cannot be the same as any**Group by**field
- 
					**Exclusive value column usage**– A value column cannot be used by both a sparkline and a data bar
- 
					**Export support**– Sparklines are included in PDF exports but not in CSV or Excel exports
- 
					**Filter behavior**– Filters applied to the table also filter sparkline data
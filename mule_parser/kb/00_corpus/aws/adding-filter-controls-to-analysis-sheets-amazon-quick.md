# Adding filter controls to analysis sheets - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/filter-controls.html](https://docs.aws.amazon.com/quick/latest/userguide/filter-controls.html)

---

When you're designing an analysis, you can add a filter to the analysis sheet near the visuals that you want to filter. It appears in the sheet as a control that dashboard viewers can use when you publish the analysis as a dashboard. The control uses the analysis theme settings so it looks like it's part of the sheet.

Filter controls share some settings with their filters. They apply to one, some, or all of the objects on the same sheet.

Use the following sections add and customize filter controls to an analysis. To learn how
		to add cross-sheet controls, see [Controls](./cross-sheet-filters.html#cross-sheet-controls).

###### Topics

## Adding filter controls

		Use the following procedure to add a filter control.

###### To add a filter control

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
				From the Quick homepage, choose **Analyses**, and then choose the analysis that you want to work with.
- 
				In the analysis, choose **Filter**.
- 
				If you don't already have some filters available, create one. For more information about creating filters, see [Adding filters](./add-a-filter-data-prep.html).
- 
				In the **Filters**pane, choose the three dots to the right of the filter that you want to add a control for, and choose**Add to sheet**.The filter control is added to the sheet, usually at the bottom. You can resize it or drag it to different positions on the sheet. You can also customize how it appears and how dashboard viewers can interact with it. For more information about customizing filter controls, see the following sections. 

## Pinning filter controls to the top of a sheet

		Use the following procedure to pin filter controls to the top of a sheet.

###### To pin a control to the top of a sheet

- 
				On the filter control that you want to move, choose the three dots next to the pencil icon and choose **Pin to top**.The filter is pinned to the top of the sheet and is collapsed. You can click it to expand it. 
- 
				(Optional) To unpin the control, expand it and hover over it at the top of the sheet until three dots appear. Choose the three dots, and then choose **Move to sheet**.

## Customizing filter controls

		Depending on the data type of the field and the type of filter, filter controls have different settings available. You can customize how they appear in the sheet and how dashboard viewers can interact with them.

###### To customize a filter control

- 
				Choose the filter control in the sheet. 
- 
				On the filter control, choose the pencil icon. If the filter control is pinned to the top of the sheet, expand it and hover your cursor over it until the three dots appear. Choose the three dots, and then choose **Edit**.
- 
				In the **Format control**pane that opens, do the following:- 
						For **Display name**, enter a name for the filter control.
- 
						(Optional) To hide the display name from the filter control, clear the check box for **Show title**.
- 
						For **Title font size**, choose the title font size that you want to use. The options range from extra small to extra large. The default setting is medium.
 
- 
						

The remaining steps depend on the type of field the control is referencing. For options by filter type, see the following sections.

### Date filters

If your filter control is from a date filter, use the following procedure to customize the remaining options.

###### To customize further options for a date filter

- 
					In the **Format control**pane, for**Style**, choose one of the following options:- 
							**Date picker – range**– Displays a set of two fields to define a time range. You can enter a date or time, or you can choose a date from the calendar control. You can also customize how you want the dates to appear in the control by entering a date token for**Date format**. For more information, see[Customizing date formats in Quick](./format-visual-date-controls.html).
- 
							**Date picker – relative**– Displays settings like the time period, its relation to the current date and time, and the option to exclude time periods. You can also customize how you want the dates to appear in the control by entering a date token for**Date format**. For more information, see[Customizing date formats in Quick](./format-visual-date-controls.html).
- 
							**Text field**– Displays a box where you can enter the top or bottom*N*date.Helper text is included in the text field control by default, but you can choose to remove it by clearing the **Show helper text in control**option.
 By default, Quick visuals are reloaded whenever a change is made to a control. For Calendar and Relative date picker controls, authors can add an **Apply**button to a control that delays visual reload until the user chooses**Apply**. This allows users to make multiple changes at a time without additional queries. This setting can be configured with the**Show an apply button**checkbox in the**Control options**section of the**Format control**pane.
- 
							
- 
					When finished, choose **Apply**.

### Text filters

If your filter control is from a text filter, for example dimensions, categories, or labels, use the following procedure to customize the remaining options.

###### To customize further options for a text filter

- 
					In the **Format control**pane, for**Style**, choose one of the following options:- 
							**Dropdown**– Displays a dropdown list with buttons that you can use to select a single value.When you select this option, you can choose the following options for **Values**:- 
									**Filter**– Displays all the values that are available in the filter.
- 
									**Specific values**– Enables you to enter the values to display, one entry per line.
 You can also choose to **Hide Select all option from the control values**. This removes the option to select or clear the selection of all values in the filter control.
- 
									
- 
							**Dropdown - multiselect**– Displays a dropdown list with boxes that you can use to select multiple values.When you select this option, you can choose the following options for **Values**:- 
									**Filter**– Displays all the values that are available in the filter.
- 
									**Specific values**– Enables you to enter the values to display, one entry per line.
 By default, Quick visuals are reloaded whenever a change is made to a control. For Multiselect dropdown controls, authors can add an **Apply**button to a control that delays visual reload until the user chooses**Apply**. This allows users to make multiple changes at a time without additional queries. This setting can be configured with the**Show an apply button**checkbox in the**Control options**section of the**Format control**pane.
- 
									
- 
							**List**– Displays a list with buttons that you can use to select a single value.When you select this option, you can choose the following options for **Values**:- 
									**Filter**– Displays all the values that are available in the filter.
- 
									**Specific values**– Enables you to enter the values to display, one entry per line.
 You can also choose the following: - 
									**Hide search bar when control is on sheet**– Hides the search bar in the filter control, so users can't search for specific values.
- 
									**Hide Select all option from the control values**– Removes the option to select or clear the selection of all values in the filter control.
 
- 
									
- 
							**List - multiselect**– Displays a list with boxes that you can use to select multiple values.When you select this option, you can choose the following options for **Values**:- 
									**Filter**– Displays all the values that are available in the filter.
- 
									**Specific values**– Enables you to enter the values to display, one entry per line.
 You can also choose the following: - 
									**Hide search bar when control is on sheet**– Hides the search bar in the filter control, so users can't search for specific values.
- 
									**Hide Select all option from the control values**– Removes the option to select or clear the selection of all values in the filter control.
 
- 
									
- 
							**Text field**– Displays a text box where you can enter a single entry. Text fields support up to 79950 characters.When you select this option, you can choose the following: - 
									**Show helper text in control**– Removes the helper text in text fields.
 
- 
									
- 
							**Text field - multiline**– Displays a text box where you can enter multiple entries. Multiline text fields support up to 79950 characters across all entries.When you select this option, you can choose the following: - 
									For **Separate values by**, choose how you want to separate values you enter into the filter control. You can choose to separate values by a line break, comma, pipe (|), or semicolon.
- 
									**Show helper text in control**– Removes the helper text in text fields.
 
- 
									
 
- 
							
- 
					When finished, choose **Apply**.

### Numeric filters

If your filter control is from a numeric filter, use the following procedure to customize the remaining options.

###### To customize further options for a numeric filter

- 
					In the **Format control**pane, for**Style**, choose one of the following options:- 
							**Dropdown**– Displays a list where you can select a single value.When you select this option, you can choose the following options for **Values**:- 
									**Filter**– Displays all the values that are available in the filter.
- 
									**Specific values**– Enables you to enter the values to display, one entry per line.
 You can also choose to **Hide Select all option from the control values**. This removes the option to select or clear the selection of all values in the filter control.- 
									**Filter**– Displays all the values that are available in the filter.
- 
									**Specific values**– Enables you to enter the values to display, one entry per line.
- 
									**Hide Select all option from the control values**– Removes the option to select or clear the selection of all values in the filter control.
 
- 
									
- 
							**List**– Displays a list with buttons that enable selecting a single value.When you select this option, you can choose the following options for **Values**:- 
									**Filter**– Displays all the values that are available in the filter.
- 
									**Specific values**– Enables you to enter the values to display, one entry per line.
 You can also choose the following: - 
									**Hide search bar when control is on sheet**– Hides the search bar in the filter control, so users can't search for specific values.
- 
									**Hide Select all option from the control values**– Removes the option to select or clear the selection of all values in the filter control.
 
- 
									
- 
							**Slider**– Displays a horizontal bar with a toggle that you can slide to change the value. If you have a ranged filter for values between a minimum and a maximum, the slider provides a toggle for each number. For sliders, you can specify the following options:- 
									**Minimum value**– Displays the smaller value at the left of the slider.
- 
									**Maximum value**– Displays the larger value at the right of the slider.
- 
									**Step size**– Enables you to set the number of increments that the bar is divided into.
 
- 
									
- 
							**Text box**– Displays a box where you can enter the value. When you select this option, you can choose the following:- 
									**Show helper text in control**– Removes the helper text in text fields.
 
- 
									
 
- 
							
- 
					When finished, choose **Apply**.

## Sorting filter control values

		Custom sort gives authors control over how values appear in dropdown and list filter controls. By default, control values are sorted alphabetically in ascending order. With custom sort, you can display values in a specific business order (such as fiscal quarters or priority levels) or sort by related metrics (such as sorting regions by total sales).

Custom sort is available for **Dropdown** (single select and
			multiselect) and **List** (single select and multiselect) control
			styles. The available sort options depend on whether the control uses specific values or
			values from a dataset column.

###### Note

Custom sort is not available for date type columns at this time. To sort date values in a logical order, use the sort by another field option with a date-related field.

### When to use custom sort

Use custom sort when you need to do the following:

- 
					**Display values in business logic order**– For example, priority levels (Critical, High, Medium, Low), fiscal quarters (Q1, Q2, Q3, Q4), or custom status workflows (New, In Progress, Review, Complete).
- 
					**Sort by related metrics**– For example, products sorted by total sales, regions sorted by customer count, categories sorted by average revenue, or departments sorted by headcount.

### Configuring custom sort

The sort configuration options depend on whether the control uses specific values or values from a dataset column.

#### Controls with specific values

When a control uses specific values that you entered manually, the following
					sort options are available in the **Sort** section of the
					**Format control** pane.

###### To configure sort for a specific values control

- 
						Choose the filter control in the sheet. 
- 
						Choose the pencil icon to open the **Format control**pane.
- 
						In the **Format control**pane, locate the**Sort**section.
- 
						Choose one of the following options: - 
								**Ascending (A–Z, 0–9)**– Sorts values in ascending order. This is the default.
- 
								**Descending (Z–A, 9–0)**– Sorts values in descending order.
- 
								**User-defined order**– Displays the values in the exact order you entered them. This preserves your custom ordering without any automatic sorting.
 
- 
								

###### Note

When a control has values from both specific values and a source entity (such as a filter or parameter), the combined list is sorted together. For user-defined order, values are appended in the order they were entered. If a value from the source cannot be sorted based on the current configuration, it is appended at the end of the list.

#### Controls with values from a dataset column

When a control displays values from a dataset column, you can sort by that field or another field in the dataset using an aggregation function. This is useful when you want to order control values by a related metric, such as sorting a list of products by total sales.

###### To configure sort for a column-based control

- 
						Choose the filter control in the sheet. 
- 
						Choose the pencil icon to open the **Format control**pane.
- 
						In the **Format control**pane, locate the**Sort**section.
- 
						Configure the following options: - 
								**Sort by control column**– Sorts the control values based on the column that the control is tied to.- 
										For **Sort direction**, choose**Ascending**or**Descending**.
- 
										For **Aggregation**, choose an aggregation function or choose**No aggregation**to sort by the raw column values.
 
- 
										
- 
								**Sort by another field**– Sorts the control values based on a different column in the dataset.- 
										For **Sort by field**, choose a column from the dataset. For calculated fields, only scalar (non-aggregated) calculated columns are available.
- 
										For **Aggregation**, choose an aggregation function to apply to the sort field. The available functions depend on the data type of the selected column. For numeric fields, you can use Sum, Average, Count, Distinct count, Min, Max, Median, Percentile, Var, Stdev, and other statistical functions. For non-numeric fields, you can use Count and Distinct count.
- 
										For **Sort direction**, choose**Ascending**or**Descending**.
 
- 
										
 
- 
								

#### Cross-sheet filter controls

You can configure sort order for cross-sheet filter controls through the cross-sheet settings. The sort configuration applies to all instances of the control across sheets.

###### To configure sort for a cross-sheet filter control

- 
						Open the cross-sheet settings for the filter. 
- 
						In the default control configuration section, locate the **Sort**settings.
- 
						Configure the sort options as described in the preceding sections. 
- 
						Choose **Apply**.

###### Note

Dashboard controls inherit the sort configuration from the analysis. Sort configuration changes are not available to dashboard readers.

## Cascading filter controls

		You can limit the values displayed in the control, so they only show values that are valid for what is selected in other controls. This is called a cascading control.

###### When creating cascading controls, the following limitations apply:

- 
				Cascading controls must be tied to dataset columns from the same dataset. 
- 
				The child control must be a dropdown or list control. 
- 
				For parameter controls, the child control must be linked to a dataset column. 
- 
				For filter controls, the child control must be linked to a filter (instead of showing only specific values). 
- 
				The parent control must be one of the following: - 
						A string, integer, or numeric parameter control. 
- 
						A string filter control (excluding top-bottom filters). 
- 
						A non-aggregated numeric filter control. 
- 
						A date filter control (excluding top-bottom filters). 
 
- 
						

###### To create a cascading control

- 
				Choose **Show relevant values only.**Note that this option might not be available for all filter control types.
- 
				In the **Show relevant values only**pane that opens, choose one or more controls from the available list.
- 
				Choose a field to match the value to. 
- 
				Choose **Update**.
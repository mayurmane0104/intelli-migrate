# Adding date filters - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/add-a-date-filter2.html](https://docs.aws.amazon.com/quick/latest/userguide/add-a-date-filter2.html)

---

You create filters on date fields by selecting the filter conditions and date values that you want to use. There are three filter types for dates:

- 
				Range – A series of dates based on a time range and comparison type. You can filter records based on whether the date field value is before or after a specified date, or within a date range. You enter date values in the format MM/DD/YYYY. You can use the following comparison types: - 
						Between – Between a start date and an end date 
- 
						After – After a specified date 
- 
						Before – Before a specified date 
- 
						Equals – On a specified date 
 For each comparison type, you can alternatively choose a rolling date relative to a period or dataset value. 
- 
						
- 
				Relative (analyses only) – A series of date and time elements based on the current date. You can filter records based on the current date and your selected unit of measure (UOM). Date filter units include years, quarters, months, weeks, days, hours, and minutes. You can exclude current period, add support for Next N filters similar to Last N with an added capability to allow for Anchor date. You can use the following comparison types: - 
						Previous – The previous UOM—for example, the previous year. 
- 
						This – This UOM, which includes all dates and times that fall within the select UOM, even if they occur in the future. 
- 
						To date *or*up to now – UOM to date, or UOM up to now. The displayed phrase adapts to the UOM that you choose. However, in all cases this option filters out data that is not between the beginning of the current UOM and the current moment.
- 
						Last *n*– The last specified number of the given UOM, which includes all of this UOM and all of the last*n*−1 UOM. For example, let's say today is May 10, 2017. You choose to use*years*as your UOM, and set Last*n*years to 3. The filtered data includes data for all of 2017, plus all of 2016, and all of 2015. If you have any data for the future dates of the current year (2017 in this example), these records are included in your dataset.
 
- 
						
- 
				Top and bottom (analyses only) – A number of date entries ranked by another field. You can show the top or bottom *n*for the type of date or time UOM you choose, based on values in another field. For example, you can choose to show the top 5 sales days based on revenue.

Comparisons are applied inclusive to the date specified. For example, if you apply the
			filter `Before 1/1/16`, the records returned include all rows with date
			values through 1/1/16 23:59:59. If you don't want to include the date specified,
			you can clear the option to **Include this date**. If you want to omit
			a time range, you can use the **Exclude the last N periods** option to
			specify the number and type of time periods (minutes, days, and so on) to filter
			out.

You can also choose to include or exclude nulls, or exclusively show rows that contain nulls in this field. If you pass in a null date parameter (one without a default value), it doesn't filter the data until you provide a value.

###### Note

If a column or attribute has no time zone information, then the client query
				engine sets the default interpretation of that date-time data. For example, suppose
				that a column contains a timestamp, rather than a timestamptz, and you are in a
				different time zone than the data's origin. In this case, the engine can render
				the timestamp differently than you expect. Amazon Quick and [SPICE](./spice.html) both use Universal Coordinated Time (UTC)
				times. 

Use the following sections to learn how to create date filters in datasets and analyses.

## Creating date filters in datasets

			Use the following procedure to create a range filter for a date field in a dataset.

###### To create a range filter for a date field in a dataset

- 
					Create a new filter using a text field. For more information about creating filters, see [Adding filters](./add-a-filter-data-prep.html).
- 
					In the **Filters**pane, choose the new filter to expand it.
- 
					For **Condition**, choose a comparison type:**Between**,**After**, or**Before**.To use **Between**as a comparison, choose**Start date**and**End date**and choose dates from the date picker controls that appear.You can choose if you want to include either or both the start and end dates in the range by selecting **Include start date**or**Include end date**.To use **Before**or**After**comparisons, enter a date or choose the date field to bring up the date picker control and choose a date instead. You can include this date (the one you chose), to exclude the last N time periods, and specify how to handle nulls.
- 
					For **Time granularity**, choose**Day**,**Hour**,**Minute**, or**Second**.
- 
					When finished, choose **Apply**.

## Creating date filters in analyses

			You can create date filters in analyses as described following.

### Creating range date filters in analyses

Use the following procedure to create a range filter for a date field in an analysis.

###### To create a range filter for a date field in an analysis

- 
						Create a new filter using a text field. For more information about creating filters, see [Adding filters](./add-a-filter-data-prep.html).
- 
						In the **Filters**pane, choose the new filter to expand it.
- 
						For **Filter type**, choose**Date & time range**.
- 
						For **Condition**, choose a comparison type:**Between**,**After**,**Before**, or**Equals**.To use **Between**as a comparison, choose**Start date**and**End date**and choose dates from the date picker controls that appear.You can choose to include either or both the start and end dates in the range by selecting **Include start date**or**Include end date**.To use a **Before**,**After**, or**Equals**comparison, enter a date or choose the date field to bring up the date picker control and choose a date instead. You can include this date (the one you chose), to exclude the last N time periods, and specify how to handle nulls.To **Set a rolling date**for your comparison, choose**Set a rolling date**.In the **Set a rolling date**pane that opens, choose**Relative date**and then select if you want to set the date to**Today**,**Yesterday**, or you can specify the**Filter condition**(start of or end of),**Range**(this, previous, or next), and**Period**(year, quarter, month, week, or day).
- 
						For **Time granularity**, choose**Day**,**Hour**,**Minute**, or**Second**.
- 
						(Optional) If you are filtering by using an existing parameter, instead of specific dates, choose **Use parameters**, then choose your parameter or parameters from the list. To use**Before**,**After**, or**Equals**comparisons, choose one date parameter. You can include this date in the range.To use **Between**, enter both the start date and end date parameters separately. You can include the start date, the end date, or both in the range.To use parameters in a filter, create them first. Usually, you create a parameter, add a control for it, and then add a filter for it. For more information, see [Parameters in Amazon Quick](./parameters-in-quicksight.html).
- 
						For **Null options**choose**Exclude nulls**,**Include nulls**, or**Nulls only**.
- 
						When finished, choose **Apply**.

### Creating relative date filters in analyses

Use the following procedure to create a relative filter for a date field in an analysis.

###### To create a relative filter for a date field in an analysis

- 
						Create a new filter using a text field. For more information about creating filters, see [Adding filters](./add-a-filter-data-prep.html).
- 
						In the **Filters**pane, choose the new filter to expand it.
- 
						For **Filter type**, choose**Relative dates**.
- 
						For **Time granularity**, choose a granularity of time that you want to filter by (days, hours, minutes).
- 
						For **Period**, choose a unit of time (years, quarters, quarters, months, weeks, days).
- 
						For **Range**, choose how you want the filter to relate to the time frame. For example, if you choose to report on months, your options are previous month, this month, month to date, last N months, and next N months.If you choose Last N or Next N years, quarters, months, weeks, or days, enter a number for **Number of**. For example, last 3 years, next 5 quarters, last 5 days.
- 
						For **Null options**choose**Exclude nulls**,**Include nulls**, or**Nulls only**.
- 
						For **Set dates relative to**, choose one of the following options:- 
								**Current date time**– If you choose this option, you can set it to**Exclude last**, and then specify the number and type of time periods.
- 
								**Date and time from a parameter**– If you choose this option, you can select an existing datetime parameter.
 
- 
								
- 
						(Optional) If you are filtering by using an existing parameter, instead of specific dates, enable **Use parameters**, then choose your parameter or parameters from the list.To use parameters in a filter, create them first. Usually, you create a parameter, add a control for it, and then add a filter for it. For more information, see [Parameters in Amazon Quick](./parameters-in-quicksight.html).
- 
						When finished, choose **Apply**.

### Creating top and bottom date filters in analyses

Use the following procedure to create a top and bottom filter for a date field in an analysis.

###### To create a top and bottom filter for a date field in an analysis

- 
						Create a new filter using a text field. For more information about creating filters, see [Adding filters](./add-a-filter-data-prep.html).
- 
						In the **Filters**pane, choose the new filter to expand it.
- 
						For **Filter type**, choose**Top and bottom**.
- 
						Select **Top**or**Bottom**.
- 
						For **Show**, enter the number of top or bottom items you want to show and choose a unit of time (years, quarters, months, weeks days, hours, minutes).
- 
						For **By**, choose a field to base the ranking on.
- 
						(Optional) Add another field as a tie breaker, if the field for **By**has duplicates. Choose**Tie breaker**, and then choose another field. To remove a tie breaker, use the delete icon.
- 
						(Optional) If you are filtering by using an existing parameter, instead of specific dates, select **Use parameters**, then choose your parameter or parameters from the list.To use a parameter for **Top and bottom**, choose an integer parameter for the number of top or bottom items to show.To use parameters in a filter, create them first. Usually, you create a parameter, add a control for it, and then add a filter for it. For more information, see [Parameters in Amazon Quick](./parameters-in-quicksight.html).
- 
						When finished, choose **Apply**.
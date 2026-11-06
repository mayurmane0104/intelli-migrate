# Changing a field data type - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/changing-a-field-data-type.html](https://docs.aws.amazon.com/quick/latest/userguide/changing-a-field-data-type.html)

---

When Quick Sight retrieves data, it assigns each field a data type based on the data in the field. The possible data types are as follows:

- 
				Date – The date data type is used for date data in a supported format. For information about the date formats Quick Sight supports, see [Data source quotas](./data-source-limits.html).
- 
				Decimal – The decimal data type is used for numeric data that requires one or more decimal places of precision, for example 18.23. The decimal data type supports values with up to four decimal places to the right of the decimal point. Values that have a higher scale than this are truncated to the fourth decimal place in two cases. One is when these values are displayed in data preparation or analyses, and one is when these values are imported into Quick Sight. For example, 13.00049 is truncated to 13.0004. 
- 
				Geospatial – The geospatial data type is used for geospatial data, for example longitude and latitude, or cities and countries. 
- 
				Integer – The int data type is used for numeric data that only contains integers, for example 39. 
- 
				String – The string data type is used for nondate alphanumeric data. 

Quick Sight reads a small sample of rows in the column to determine the data type. The data type that occurs most in the small sample size is the suggested type. In some cases, there might be blank values (treated as strings by Quick Sight) in a column that contains mostly numbers. In these cases, it might be that the String data type is the most frequent type in the sample set of rows. You can manually modify the data type of the column to make it integer. Use the following procedures to learn how.

## Changing a field data type during data prep

			During data preparation, you can change the data type of any field from the data
				source. On the **Change data type** menu, you can change calculated
				fields that don't include aggregations to geospatial types. You can make other
				changes to the data type of a calculated field by modifying its expression directly.
				Quick Sight converts the field data according to the data type that you choose.
				Rows that contain data that is incompatible with that data type are skipped. For
				example, suppose that you convert the following field from String to Integer.

`10020 36803 14267a 98457 78216b`

All records containing alphabetic characters in that field are skipped, as shown following.

`10020 36803 98457`

If you have a database dataset with fields whose data types aren't supported by
				Quick Sight, use a SQL query during data preparation. Then use `CAST` or
					`CONVERT` commands (depending on what is supported by the source
				database) to change the field data types. For more information about adding a SQL
				query during data preparation, see [Using SQL to customize data](./adding-a-SQL-query.html). For more information about how different
				source data types are interpreted by Quick Sight, see [Supported data types from external data sources](./supported-data-types-and-values.html#supported-data-types).

You might have numeric fields that act as dimensions rather than metrics, for
				example ZIP codes and most ID numbers. In these cases, it's helpful to give
				them a string data type during data preparation. Doing this lets Quick Sight
				understand that they are not useful for performing mathematical calculations and can
				only be aggregated with the `Count` function. For more information about
				how Quick Sight uses dimensions and measures, see [Setting fields as a dimensions or measures](./setting-dimension-or-measure.html).

In [SPICE](./spice.html), numbers converted from
				numeric into an integer are truncated by default. If you want to round your numbers
				instead, you can create a calculated field using the [round](./round-function.html) function. To see whether numbers are rounded or
				truncated before they are ingested into SPICE, check your database
				engine.

###### To change a field data type during data prep

- 
					From the Quick Sight homepage, choose **Data**at left. In the**Data**tab, choose the dataset that you want, and then choose**Edit dataset**.
- 
					In the data preview pane, choose the data type icon under the field you want to change. 
- 
					Choose the target data type. Only data types other than the one currently in use are listed. 

## Changing a field data type in an analysis

			You can use the **Field list** pane, visual field wells, or
				on-visual editors to change numeric field data types within the context of an
				analysis. Numeric fields default to displaying as numbers, but you can choose to
				have them display as currency or as a percentage instead. You can't change the data
				types for string or date fields.

Changing a field's data type in an analysis changes it for all visuals in the analysis that use that dataset. However, it doesn't change it in the dataset itself.

###### Note

If you are working in a pivot table visual, applying a table calculation changes the data type of the cell values in some cases. This type of change occurs if the data type doesn't make sense with the applied calculation.

For example, suppose that you apply the `Rank` function to a
					numeric field that you modified to use a currency data type. In this case, the
					cell values display as numbers rather than currency. Similarly, if you apply the
						`Percent difference` function instead, the cell values display as
					percentages rather than currency. 

###### To change a field's data type

- 
					Choose one of the following options: - 
							In the **Field list**pane, hover over the numeric field that you want to change. Then choose the selector icon to the right of the field name.
- 
							On any visual that contains an on-visual editor associated with the numeric field that you want to change, choose that on-visual editor. 
- 
							Expand the **Field wells**pane, and then choose the field well associated with the numeric field that you want to change.
 
- 
							
- 
					Choose **Show as**, and then choose**Number**,**Currency**, or**Percent**.
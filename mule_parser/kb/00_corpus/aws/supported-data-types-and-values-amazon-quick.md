# Supported data types and values - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/supported-data-types-and-values.html](https://docs.aws.amazon.com/quick/latest/userguide/supported-data-types-and-values.html)

---

Amazon Quick Sight currently supports the following primitive data types: `Date`,
				`Decimal`, `Integer`, and `String`. The following
			data types are supported in SPICE: `Date`,
				`Decimal-fixed`, `Decimal-float`, `Integer`, and
				`String`. Quick Sight accepts Boolean values by promoting them to
			integers. It can also derive geospatial data types. Geospatial data types use metadata
			to interpret the physical data type. Latitude and longitude are numeric. All other
			geospatial categories are strings. 

Make sure that any table or file that you use as a data source contains only fields that can be implicitly converted to these data types. Amazon Quick Sight skips any fields or columns that can't be converted. If you get an error that says "fields were skipped because they use unsupported data types", alter your query or table to remove or recast unsupported data types.

## String and text data

			Fields or columns that contain characters are called *strings*.
				A field with the data type of `STRING` can initially contain almost any
				type of data. Examples include names, descriptions, phone numbers, account numbers,
				JSON data, cities, post codes, dates, and numbers that can be used to calculate.
				These types are sometimes called textual data in a general sense, but not in a
				technical sense. Quick Sight doesn't support binary and character large objects
				(BLOBs) in dataset columns. In the Quick Sight documentation, the term "text"
				always means "string data". 

The first time you query or import the data, Quick Sight tries to interpret the data that it identifies as other types, for example dates and numbers. It's a good idea to verify that the data types assigned to your fields or columns are correct.

For each string field in imported data, Quick Sight uses a field length of 8 bytes plus the UTF-8 encoded character length. Amazon Quick Sight supports UTF-8 file encoding, but not UTF-8 (with BOM).

## Date and time data

			Fields with a data type of `Date` also include time data, and are also
				known as `Datetime` fields. Quick Sight supports dates and times that
				use [supported date formats](#supported-date-formats). 

Quick Sight uses UTC time for querying, filtering, and displaying date data. When
				date data doesn't specify a time zone, Quick Sight assumes UTC values. When date
				data does specify a time zone, Quick Sight converts it to display in UTC time. For
				example, a date field with a time zone offset like
					`2015-11-01T03:00:00-08:00` is converted to UTC and
				displayed in Amazon Quick Sight as `2015-11-01T15:30:00`. 

For each `DATE` field in imported data, Quick Sight uses a field
				length of 8 bytes. Quick Sight supports UTF-8 file encoding, but not UTF-8 (with
				BOM).

## Numeric data

			Numeric data includes integers and decimals. Integers with a data type of
					`INT` are negative or positive numbers that don't have a decimal
				place. Quick Sight doesn't distinguish between large and small integers. Integers
				over a value of `9007199254740991` or `2^53 - 1` might not
				display exactly or correctly in a visual.

Decimals with the data type of `Decimal` are negative or positive
				numbers that contain at least one decimal place before or after the decimal point.
				When you choose Direct Query mode, all non-integer decimal types are marked as
					`Decimal` and the underlying engine handles the precision of the
				datapoint based on the data source's supported behaviors. For more information
				on supported data source types, see [Supported data types and values](./supported-data-types-and-values.html).

When you store your dataset in SPICE, you can choose to store your
				decimal values as `fixed` or `float` decimal types.
					`Decimal-fixed` data types use the format of decimal
					(`18,4`) that allow 18 digits total and up to 4 digits after the
				decimal point. `Decimal-fixed` data types are a good choice to conduct
				exact mathematical operations, but Quick Sight rounds the value to the nearest ten
				thousandth place when the value is ingested into SPICE.

`Decimal-float` data types provide approximately 16 significant digits
				of accuracy to a value. The significant digits can be on either side of the decimal
				point to support numbers with many decimal places and higher numbers at the same
				time. For example, the `Decimal-float` data type supports the number
					`12345.1234567890` or the number `1234567890.12345`. If
				you work with very small numbers that are close to `0`, the
					`Decimal-float` data type supports up to 15 digits to the right of
				the decimal point, for example `0.123451234512345`. The maximum value
				that this data type supports is `1.8 * 10^308` to minimize the
				probability of an overflow error with your data set.

The `Decimal-float` data type is inexact and some values are stored as
				approximations instead of the real value. This may result in slight descrepencies
				when you store and return some specific values. The following considerations apply
				to the `Decimal-float` data type.

- 
					If the dataset that you're using comes from an Amazon S3 data source, SPICE assigns the `Decimal-float`decimal type to all numeric decimal values.
- 
					If the dataset that you're using comes from a database, SPICE uses the decimal type that the value is assigned in the database. For example, if the value is assigned a fixed-point numeric value in the database, the value will be a `Decimal-fixed`type in SPICE.

For existing SPICE datasets that contain fields that can be
				converted to the `Decimal-float` data type, a pop-up appears in the
					**Edit dataset** page. To convert fields of an existing dataset
				to the `Decimal-float` data type, choose **UPDATE
					FIELDS**. If you don't want to opt in, choose **DO NOT UPDATE
					FIELDS**. The **Update fields** pop up appears every
				time you open the **Edit dataset** page until the dataset is saved
				and published.

## Supported data types from external data sources

			The following table lists data types that are supported when using the following data sources with Amazon Quick Sight.

| Database engine or source | Numeric data types | String data types | Datetime data types | Boolean data types | 
|---|---|---|---|---|
| 
									 | 
 | 
 | 
 | 
 | 
| 
 | 
 | 
 | 
 | |
| 
									 | 
 | 
 | 
 | 
 | 
| 
 | 
 | 
 | 
 | bit | 
| 
									 | 
 | 
 | 
 | 
 | 
| 
									 | 
 | 
 | 
 | 
 | 
| 
									 | 
 | 
 | 
 | 
 | 
| 
									 | 
 | 
 | 
 | 
 | 

### Supported date formats

Amazon Quick Sight supports the date and time formats described in this section. Before
					you add data to Amazon Quick Sight, check if your date format is compatible. If you need to
					use an unsupported format, see [Using unsupported or custom dates](./using-unsupported-dates.html).

The supported formats vary depending on the data source type, as follows:

| Data source | Clocks | Date formats | 
|---|---|---|
| File uploads Amazon S3 sources Athena Salesforce | Both 24-hour and 12-hour clocks | Supported date and time formats are described in the Joda API documentation. For a complete list of Joda date formats, see  For datasets stored in memory (SPICE),
										Amazon Quick Sight supports dates in the following range:  | 
| Relational databases sources | 24-hour clock only | The following data and time formats: 
 | 

### Unsupported values in data

If a field contains values that don't conform with the data type that Amazon Quick Sight assigns to the field, the rows containing those values are skipped. For example, take the following source data.

`Sales ID Sales Date Sales Amount -------------------------------------- 001 10/14/2015 12.43 002 5/3/2012 25.00 003 Unknown 18.17 004 3/8/2009 86.02`

Amazon Quick Sight interprets `Sales Date` as a date field and drops
					the row containing a nondate value, so only the following rows are
					imported.

`Sales ID Sales Date Sales Amount -------------------------------------- 001 10/14/2015 12.43 002 5/3/2012 25.00 004 3/8/2009 86.02`

In some cases, a database field might contain values that the JDBC driver
					can't interpret for the source database engine. In such cases, the
					uninterpretable values are replaced by null so that the rows can be imported.
					The only known occurrence of this issue is with MySQL date, datetime, and
					timestamp fields that have all-zero values, for example ```
0000-00-00
						00:00:00
```
. For example, take the following source data.

`Sales ID Sales Date Sales Amount --------------------------------------------------- 001 2004-10-12 09:14:27 12.43 002 2012-04-07 12:59:03 25.00 003 0000-00-00 00:00:00 18.17 004 2015-09-30 01:41:19 86.02`

In this case, the following data is imported.

`Sales ID Sales Date Sales Amount --------------------------------------------------- 001 2004-10-12 09:14:27 12.43 002 2012-04-07 12:59:03 25.00 003 (null) 18.17 004 2015-09-30 01:41:19 86.02`
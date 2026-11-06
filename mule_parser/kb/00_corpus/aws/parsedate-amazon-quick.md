# parseDate - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/parseDate-function.html](https://docs.aws.amazon.com/quick/latest/userguide/parseDate-function.html)

---

`parseDate` parses a string to determine if it contains a date value,
				and returns a standard date in the format `yyyy-MM-ddTkk:mm:ss.SSSZ`
				(using the format pattern syntax specified in [Class DateTimeFormat](http://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html) in the Joda project documentation), for example
				2015-10-15T19:11:51.003Z. This function returns all rows that contain a date in a
				valid format and skips any rows that don't, including rows that contain null
				values.

Quick supports dates in the range from Jan 1, 1900 00:00:00 UTC to Dec
				31, 2037 23:59:59 UTC. For more information, see [Supported date formats](https://docs.aws.amazon.com/quicksight/latest/user/supported-date-formats.html).

## Syntax

				
				`parseDate(``expression`, [`'format'`])

## Arguments

				- 
							*expression*
- 
							The expression must be a string. It can be the name of a field that uses the string data type, a literal value like `'1/1/2016'`, or a call to another function that outputs a string.
- 
							*format*
- 
							(Optional) A string containing the format pattern that *date_string*must match. For example, if you are using a field with data like`01/03/2016`, you specify the format 'MM/dd/yyyy'. If you don't specify a format, it defaults to`yyyy-MM-dd`. Rows whose data doesn't conform to*format*are skipped.Different date formats are supported based on the type of dataset used. Use the following table to see details of supported date formats. Date source type Supported date formats File, Amazon Athena, and Salesforce data sets All date format patterns specified in [Supported date formats](https://docs.aws.amazon.com/quicksight/latest/user/supported-date-formats.html).Direct query of Amazon Aurora, MariaDB, and MySQL databases - 
												MM/dd/yyyy 
- 
												dd/MM/yyyy 
- 
												yyyy/MM/dd 
- 
												MMM/dd/yyyy 
- 
												dd/MMM/yyyy 
- 
												yyyy/MMM/dd 
- 
												MM/dd/yyyy HH:mm:ss 
- 
												dd/MM/yyyy HH:mm:ss 
- 
												yyyy/MM/dd HH:mm:ss 
- 
												MMM/dd/yyyy HH:mm:ss 
- 
												dd/MMM/yyyy HH:mm:ss 
- 
												yyyy/MMM/dd HH:mm:ss 
- 
												MM-dd-yyyy 
- 
												dd-MM-yyyy 
- 
												yyyy-MM-dd 
- 
												MMM-dd-yyyy 
- 
												dd-MMM-yyyy 
- 
												yyyy-MMM-dd 
- 
												MM-dd-yyyy HH:mm:ss 
- 
												dd-MM-yyyy HH:mm:ss 
- 
												yyyy-MM-dd HH:mm:ss 
- 
												MMM-dd-yyyy HH:mm:ss 
- 
												dd-MMM-yyyy HH:mm:ss 
- 
												yyyy-MMM-dd HH:mm:ss 
- 
												MM/dd/yyyy HH:mm:ss.SSS 
- 
												dd/MM/yyyy HH:mm:ss.SSS 
- 
												yyyy/MM/dd HH:mm:ss.SSS 
- 
												MMM/dd/yyyy HH:mm:ss.SSS 
- 
												dd/MMM/yyyy HH:mm:ss.SSS 
- 
												yyyy/MMM/dd HH:mm:ss.SSS 
- 
												MM-dd-yyyy HH:mm:ss.SSS 
- 
												dd-MM-yyyy HH:mm:ss.SSS 
- 
												yyyy-MM-dd HH:mm:ss.SSS 
- 
												MMM-dd-yyyy HH:mm:ss.SSS 
- 
												dd-MMM-yyyy HH:mm:ss.SSS 
- 
												yyyy-MMM-dd HH:mm:ss.SSS 
 Direct query of Snowflake - 
												dd/MM/yyyy 
- 
												dd/MM/yyyy HH:mm:ss 
- 
												dd-MM-yyyy 
- 
												dd-MM-yyyy HH:mm:ss 
- 
												MM/dd/yyyy 
- 
												MM/dd/yyyy HH:mm:ss 
- 
												MM-dd-yyyy 
- 
												MM-dd-yyyy HH:mm:ss 
- 
												yyyy/MM/dd 
- 
												yyyy/MM/dd HH:mm:ss 
- 
												yyyy-MM-dd 
- 
												yyyy-MM-dd HH:mm:ss 
- 
												MM/dd/yyyy HH:mm:ss.SSS 
- 
												dd/MM/yyyy HH:mm:ss.SSS 
- 
												yyyy/MM/dd HH:mm:ss.SSS 
- 
												MMM/dd/yyyy HH:mm:ss.SSS 
- 
												dd/MMM/yyyy HH:mm:ss.SSS 
- 
												yyyy/MMM/dd HH:mm:ss.SSS 
- 
												MM-dd-yyyy HH:mm:ss.SSS 
- 
												dd-MM-yyyy HH:mm:ss.SSS 
- 
												yyyy-MM-dd HH:mm:ss.SSS 
- 
												MMM-dd-yyyy HH:mm:ss.SSS 
- 
												dd-MMM-yyyy HH:mm:ss.SSS 
- 
												yyyy-MMM-dd HH:mm:ss.SSS 
 Direct query of Microsoft SQL Server databases - 
												dd-MM-yyyy 
- 
												MM/dd/yyyy 
- 
												dd/MM/yyyy 
- 
												yyyy/MM/dd 
- 
												MMM/dd/yyyy 
- 
												dd/MMM/yyyy 
- 
												yyyy/MMM/dd 
- 
												dd/MM/yyyy HH:mm:ss 
- 
												yyyy/MM/dd HH:mm:ss 
- 
												MMM/dd/yyyy HH:mm:ss 
- 
												dd/MMM/yyyy HH:mm:ss 
- 
												yyyy/MMM/dd HH:mm:ss 
- 
												MM-dd-yyyy 
- 
												yyyy-MM-dd 
- 
												MMM-dd-yyyy 
- 
												yyyy-MMM-dd 
- 
												MM-dd-yyyy HH:mm:ss 
- 
												dd-MM-yyyy HH:mm:ss 
- 
												yyyy-MM-dd HH:mm:ss 
- 
												MMM-dd-yyyy HH:mm:ss 
- 
												dd-MMM-yyyy HH:mm:ss 
- 
												yyyy-MMM-dd HH:mm:ss 
- 
												MM/dd/yyyy HH:mm:ss.SSS 
- 
												dd/MM/yyyy HH:mm:ss.SSS 
- 
												yyyy/MM/dd HH:mm:ss.SSS 
- 
												MMM/dd/yyyy HH:mm:ss.SSS 
- 
												dd/MMM/yyyy HH:mm:ss.SSS 
- 
												yyyy/MMM/dd HH:mm:ss.SSS 
- 
												MM-dd-yyyy HH:mm:ss.SSS 
- 
												dd-MM-yyyy HH:mm:ss.SSS 
- 
												yyyy-MM-dd HH:mm:ss.SSS 
- 
												MMM-dd-yyyy HH:mm:ss.SSS 
- 
												dd-MMM-yyyy HH:mm:ss.SSS 
- 
												yyyy-MMM-dd HH:mm:ss.SSS 
 Direct query of Amazon Redshift or PostgreSQL databases Also, datasets from any DBMS that are stored in Quick [SPICE](./spice.html)- 
												MM/dd/yyyy 
- 
												dd/MM/yyyy 
- 
												yyyy/MM/dd 
- 
												MMM/dd/yyyy 
- 
												dd/MMM/yyyy 
- 
												yyyy/MMM/dd 
- 
												MM/dd/yyyy HH:mm:ss 
- 
												dd/MM/yyyy HH:mm:ss 
- 
												yyyy/MM/dd HH:mm:ss 
- 
												MMM/dd/yyyy HH:mm:ss 
- 
												dd/MMM/yyyy HH:mm:ss 
- 
												yyyy/MMM/dd HH:mm:ss 
- 
												MM-dd-yyyy 
- 
												dd-MM-yyyy 
- 
												yyyy-MM-dd 
- 
												MMM-dd-yyyy 
- 
												dd-MMM-yyyy 
- 
												yyyy-MMM-dd 
- 
												MM-dd-yyyy HH:mm:ss 
- 
												dd-MM-yyyy HH:mm:ss 
- 
												yyyy-MM-dd HH:mm:ss 
- 
												MMM-dd-yyyy HH:mm:ss 
- 
												dd-MMM-yyyy HH:mm:ss 
- 
												yyyy-MMM-dd HH:mm:ss 
- 
												yyyyMMdd'T'HHmmss 
- 
												yyyy-MM-dd'T'HH:mm:ss 
- 
												MM/dd/yyyy HH:mm:ss.SSS 
- 
												dd/MM/yyyy HH:mm:ss.SSS 
- 
												yyyy/MM/dd HH:mm:ss.SSS 
- 
												MMM/dd/yyyy HH:mm:ss.SSS 
- 
												dd/MMM/yyyy HH:mm:ss.SSS 
- 
												yyyy/MMM/dd HH:mm:ss.SSS 
- 
												MM-dd-yyyy HH:mm:ss.SSS 
- 
												dd-MM-yyyy HH:mm:ss.SSS 
- 
												yyyy-MM-dd HH:mm:ss.SSS 
- 
												MMM-dd-yyyy HH:mm:ss.SSS 
- 
												dd-MMM-yyyy HH:mm:ss.SSS 
- 
												yyyy-MMM-dd HH:mm:ss.SSS 
 
- 
												

## Return type

				Date

## Example

				The following example evaluates `prodDate` to determine if it
					contains date values.

`parseDate(prodDate, 'MM/dd/yyyy')`The following are the given field values.

```
prodDate
--------
01-01-1999
12/31/2006
1/18/1982 
7/4/2010 
```
For these field values, the following rows are returned.

```
12-31-2006T00:00:00.000Z
01-18-1982T00:00:00.000Z
07-04-2010T00:00:00.000Z 
```
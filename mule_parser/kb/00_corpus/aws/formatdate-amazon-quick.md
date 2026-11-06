# formatDate - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/formatDate-function.html](https://docs.aws.amazon.com/quick/latest/userguide/formatDate-function.html)

---

`formatDate` formats a date using a pattern you specify. When you are
				preparing data, you can use `formatDate` to reformat the
				date. To reformat a date in an analysis, you choose the format option
				from the context menu on the date field.

## Syntax

				
				`formatDate(``date`, [`'format'`])

## Arguments

				- 
							*date*
- 
							A date field or a call to another function that outputs a date. 
- 
							*format*
- 
							(Optional) A string containing the format pattern to apply. This argument accepts the format patterns specified in [Supported date formats](https://docs.aws.amazon.com/quicksight/latest/user/supported-date-formats.html).If you don't specify a format, this string defaults to yyyy-MM-dd **T**kk:mm:ss:SSS.

## Return type

				String

## Example

				The following example formats a UTC date.

`formatDate(orderDate, 'dd-MMM-yyyy')`The following are the given field values.

```
order date      
=========
2012-12-14T00:00:00.000Z  
2013-12-29T00:00:00.000Z
2012-11-15T00:00:00.000Z
```
For these field values, the following values are returned.

```
13 Dec 2012
28 Dec 2013
14 Nov 2012
```
## Example

				If the date contains single quotes or apostrophes, for example
						`yyyyMMdd'T'HHmmss`, you can handle this date format by using one
					of the following methods.

- 
						Enclose the entire date in double quotes, as shown in the following example: `formatDate({myDateField},``"`yyyyMMdd`'`T`'`HHmmss`"`)
- 
						Escape the single quotes or apostrophes by adding a backslash ( `\`) to the left of them, as shown in the following example:`formatDate({myDateField},``'`yyyyMMdd`\'`T`\'`HHmmss`'`)
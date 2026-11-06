# MS Access Weekday() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_weekday.asp](https://www.w3schools.com/sql/func_msaccess_weekday.asp)

---

# MS Access Weekday() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the weekday number for a date:

```
  SELECT Weekday(#05/17/2017#); 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_weekday&ss=-1)

## Definition and Usage

The Weekday() function returns the weekday number for a given date.

This function returns an integer between 1 and 7.

## Syntax

```
  Weekday(
```
*date*, *firstdayofweek*)
## Parameter Values

| Parameter | Description | 
|---|---|
| date | Required. A valid date | 
| firstdayofweek | Optional. Specifies the first day of the week.
    Can be one of the following values: 
 | 

## Technical Details

| Works in: | From Access 2000 | 
|---|

Ad

## More Examples

### Example

Return the weekday number for the specified date, setting Monday as the first day of week:

```
  SELECT Weekday(#05/17/2017#, 2); 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_weekday3&ss=-1)
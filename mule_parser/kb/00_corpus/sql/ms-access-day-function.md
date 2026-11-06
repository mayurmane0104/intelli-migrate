# MS Access Day() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_day.asp](https://www.w3schools.com/sql/func_msaccess_day.asp)

---

# MS Access Day() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the day of the month for the date:

```
  SELECT Day(#05/17/2017#); 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_day&ss=-1)

## Definition and Usage

The Day() function returns the day of the month for a given date.

This function returns an integer between 1 and 31.

## Syntax

```
Day(
```
*date*)
## Parameter Values

| Parameter | Description | 
|---|---|
| date | Required. A numeric or string expression that can represent a valid date | 

## Technical Details

| Works in: | From Access 2000 | 
|---|

Ad

Ad

## More Examples

### Example

Return the day of the month for the "BirthDay" column in "Employees":

```
  SELECT Day(BirthDate) FROM Employees; 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_day3&ss=-1)
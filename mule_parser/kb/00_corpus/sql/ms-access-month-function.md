# MS Access Month() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_month.asp](https://www.w3schools.com/sql/func_msaccess_month.asp)

---

# MS Access Month() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the month part for a specified date:

```
  SELECT Month(#05/17/2017#); 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_month&ss=-1)

## Definition and Usage

The Month() function returns the month part for a given date.

This function returns an integer between 1 and 12.

## Syntax

```
  Month(
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

## More Examples

### Example

Return the month part of the "BirthDay" column in "Employees":

```
  SELECT Month(BirthDate) FROM Employees; 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_month3&ss=-1)
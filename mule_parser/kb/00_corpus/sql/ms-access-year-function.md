# MS Access Year() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_year.asp](https://www.w3schools.com/sql/func_msaccess_year.asp)

---

# MS Access Year() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the year part of a specified date:

```
  SELECT Year(#05/17/2017#); 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_year&ss=-1)

## Definition and Usage

The Year() function returns the year part of a given date.

This function returns an integer between 100 and 9999.

## Syntax

```
  Year(
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

Return the year part of the "BirthDate" column in "Employees":

```
  SELECT Year(BirthDate) FROM Employees; 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_year3&ss=-1)
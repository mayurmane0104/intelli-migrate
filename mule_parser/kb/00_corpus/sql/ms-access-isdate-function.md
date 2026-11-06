# MS Access IsDate() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_isdate.asp](https://www.w3schools.com/sql/func_msaccess_isdate.asp)

---

# MS Access IsDate() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Check whether the expression can be converted to a date:

```
  SELECT 
  IsDate(Now()); 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_isdate&ss=-1)

## Definition and Usage

The IsDate() function checks whether an expression can be converted to a date.

This function returns a Boolean value. TRUE (-1) indicates that the expression is a valid date, and FALSE (0) indicates that the expression is not a valid date.

## Syntax

```
  IsDate(
```
*expression*)
## Parameter Values

| Parameter | Description | 
|---|---|
| expression | Required. The value to test | 

## Technical Details

| Works in: | From Access 2000 | 
|---|

Ad

## More Examples

### Example

Return TRUE if the expression is a valid date, otherwise FALSE:

```
  SELECT
  IsDate("Hello"); 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_isdate2&ss=-1)

### Example

Return TRUE if the expression is a valid date, otherwise FALSE:

```
  SELECT
  IsDate("August 25, 2017"); 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_isdate3&ss=-1)

### Example

Return TRUE if the expression is a valid date, otherwise FALSE:

```
  SELECT IsDate(#25/8/2017#); 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_isdate4&ss=-1)
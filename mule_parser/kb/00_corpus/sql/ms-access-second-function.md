# MS Access Second() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_second.asp](https://www.w3schools.com/sql/func_msaccess_second.asp)

---

# MS Access Second() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the seconds part of a specified time:

```
  SELECT 
  Second(#14:48:23#); 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_second&ss=-1)

## Definition and Usage

The Second() function returns the seconds part of a time/datetime.

This function returns an integer between 0 and 59.

## Syntax

```
  Second(
```
*time*)
## Parameter Values

| Parameter | Description | 
|---|---|
| time | Required. A numeric or string expression that can represent a valid time/datetime | 

## Technical Details

| Works in: | From Access 2000 | 
|---|

Ad

## More Examples

### Example

Return the seconds part of a specified datetime:

```
  SELECT 
  Second(#24/10/2016 11:18:34 PM#); 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_second3&ss=-1)
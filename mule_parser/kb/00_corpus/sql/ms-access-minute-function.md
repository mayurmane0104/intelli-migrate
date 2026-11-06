# MS Access Minute() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_minute.asp](https://www.w3schools.com/sql/func_msaccess_minute.asp)

---

# MS Access Minute() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the minute part of a specified time:

```
  SELECT 
  Minute(#14:48:23#); 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_minute&ss=-1)

## Definition and Usage

The Minute() function returns the minute part of a time/datetime.

This function returns an integer between 0 and 59.

## Syntax

```
  Minute(
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

Return the minute part of a specified datetime:

```
  SELECT 
  Minute(#24/10/2016 11:18:34 PM#); 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_minute3&ss=-1)
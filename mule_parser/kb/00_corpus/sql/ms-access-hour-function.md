# MS Access Hour() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_hour.asp](https://www.w3schools.com/sql/func_msaccess_hour.asp)

---

# MS Access Hour() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the hour for a specified time:

```
  SELECT 
  Hour(#14:48:23#); 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_hour&ss=-1)

## Definition and Usage

The Hour() function returns the hour part of a time/datetime.

This function returns an integer between 0 and 23.

## Syntax

```
  Hour(
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

Return the hour for a specified datetime:

```
  SELECT Hour(#24/10/2016 11:18:34 PM#); 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_hour3&ss=-1)
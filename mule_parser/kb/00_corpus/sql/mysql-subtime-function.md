# MySQL SUBTIME() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_subtime.asp](https://www.w3schools.com/sql/func_mysql_subtime.asp)

---

# MySQL SUBTIME() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Subtract 5.000001 seconds and return the datetime:

```
  SELECT SUBTIME("2017-06-15 10:24:21.000004", "5.000001"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_subtime)

## Definition and Usage

The SUBTIME() function subtracts time from a time/datetime expression and then returns the new time/datetime.

## Syntax

```
  SUBTIME(
```
*datetime*, *time_interval*)
## Parameter Values

| Parameter | Description | 
|---|---|
| datetime | Required. The time or datetime to be modified | 
| time_interval | Required. The time interval to subtract from datetime. Both positive and negative values are allowed | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

Ad

## More Examples

### Example

Subtract 3 hours, 2 minutes, 5.000001 seconds and return the datetime:

```
  SELECT SUBTIME("2017-06-15 10:24:21.000004", "3:2:5.000001"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_subtime2)

### Example

Subtract 3 minutes and return the time:

```
  SELECT SUBTIME("10:24:21", "300"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_subtime5)

### Example

Add 3 hours, 2 minutes, and 5 seconds, and return the time:

```
  SELECT SUBTIME("10:24:21", "-3:2:5"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_subtime4)
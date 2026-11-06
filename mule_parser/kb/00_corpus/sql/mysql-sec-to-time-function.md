# MySQL SEC_TO_TIME() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_sec_to_time.asp](https://www.w3schools.com/sql/func_mysql_sec_to_time.asp)

---

# MySQL SEC_TO_TIME() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return a time value based on a specified seconds value:

```
SELECT SEC_TO_TIME(1); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_sec_to_time)

## Definition and Usage

The SEC_TO_TIME() function returns a time value (in format HH:MM:SS) based on the specified seconds.

## Syntax

```
  SEC_TO_TIME(
```
*seconds*)
## Parameter Values

| Parameter | Description | 
|---|---|
| seconds | Required. The number of seconds. Both positive or negative values are allowed | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

## More Examples

### Example

Return a time value based on a specified seconds value:

```
SELECT SEC_TO_TIME(-6897); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_sec_to_time2)

Ad
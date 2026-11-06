# MySQL MAKETIME() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_maketime.asp](https://www.w3schools.com/sql/func_mysql_maketime.asp)

---

# MySQL MAKETIME() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Create and return a time value based on an hour, minute, and second value:

```
  SELECT MAKETIME(11, 35, 
  4); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_maketime)

## Definition and Usage

The MAKETIME() function creates and returns a time based on an hour, minute, and second value.

## Syntax

```
  MAKETIME(
```
*hour*, *minute*, *
  second*)
  
## Parameter Values

| Parameter | Description | 
|---|---|
| hour | Required. The hour value | 
| minute | Required. The minute value | 
| second | Required. The seconds value | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

Ad

Ad

## More Examples

### Example

Create and return a time value based on an hour, minute, and second value:

```
  SELECT MAKETIME(16, 
  1, 0); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_maketime2)

### Example

Create and return a time value based on an hour, minute, and second value:

```
  SELECT MAKETIME(21, 
  59, 59); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_maketime3)

### Example

Create and return a time value based on an hour, minute, and second value:

```
  SELECT MAKETIME(838, 
  59, 59); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_maketime4)
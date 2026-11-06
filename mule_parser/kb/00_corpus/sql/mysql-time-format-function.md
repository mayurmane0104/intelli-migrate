# MySQL TIME_FORMAT() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_time_format.asp](https://www.w3schools.com/sql/func_mysql_time_format.asp)

---

# MySQL TIME_FORMAT() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Format a time:

```
  SELECT TIME_FORMAT("19:30:10", "%H %i %s"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_time_format)

## Definition and Usage

The TIME_FORMAT() function formats a time by a specified format.

## Syntax

```
  TIME_FORMAT(
```
*time*, *format*)
  
## Parameter Values

| Parameter | Description | ||||||||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| time | Required. The time to be formatted | ||||||||||||||||||||||
| format | Required. The format to use. Can be one or a 
    combination of the following: 
 | 

Ad

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|
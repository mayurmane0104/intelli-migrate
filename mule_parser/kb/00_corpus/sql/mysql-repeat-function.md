# MySQL REPEAT() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_repeat.asp](https://www.w3schools.com/sql/func_mysql_repeat.asp)

---

# MySQL REPEAT() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Repeat a string 3 times:

```
  SELECT REPEAT("SQL Tutorial", 3); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_repeat)

## Definition and Usage

The REPEAT() function repeats a string as many times as specified.

## Syntax

```
  REPEAT(
```
*string*, *number*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string | Required. The string to repeat | 
| number | Required. The number of times to repeat the string | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

Ad

## More Examples

### Example

Repeat the text in CustomerName 2 times:

```
  SELECT REPEAT(CustomerName, 
  2)
FROM Customers; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_repeat2)
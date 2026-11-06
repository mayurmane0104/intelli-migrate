# SQL Server ROUND() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_round.asp](https://www.w3schools.com/sql/func_sqlserver_round.asp)

---

# SQL Server ROUND() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Round the number to 2 decimal places:

```
  SELECT ROUND(235.415, 2) AS RoundValue; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_round)

## Definition and Usage

The ROUND() function rounds a number to a specified number of decimal places.

**Tip:** Also look at the [FLOOR()](func_sqlserver_floor.asp) and 
[CEILING()](func_sqlserver_ceiling.asp) functions.

## Syntax

```
  ROUND(
```
*number*, *decimals*, *operation*)
## Parameter Values

| Parameter | Description | 
|---|---|
| number | Required. The number to be rounded | 
| decimals | Required. The number of decimal places to round numberto | 
| operation | Optional. If 0, it rounds the result to the number of decimal. 
    If 
    another value than 0, it truncates the result to the number of
    decimals. Default value is 0 | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

Ad

## More Examples

### Example

Round the number to 2 decimal places, and also use the *operation* 
parameter:

```
  SELECT ROUND(235.415, 2, 1) AS RoundValue; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_round2)

### Example

Round the number to -1 decimal place:

```
  SELECT ROUND(235.415, -1) AS RoundValue; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_round3)
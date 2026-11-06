# SQL Server CEILING() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_ceiling.asp](https://www.w3schools.com/sql/func_sqlserver_ceiling.asp)

---

# SQL Server CEILING() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the smallest integer value that is greater than or equal to a number:

```
  SELECT CEILING(25.75) AS CeilValue; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_ceiling)

## Definition and Usage

The CEILING() function returns the smallest integer value that is larger than or equal to a number.

**Tip:** Also look at the [FLOOR()](func_sqlserver_floor.asp) and 
[ROUND()](func_sqlserver_round.asp) functions.

## Syntax

```
  CEILING(
```
*number*)
## Parameter Values

| Parameter | Description | 
|---|---|
| number | Required. A numeric value | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

Ad

## More Examples

### Example

Return the smallest integer value that is greater than or equal to a number:

```
SELECT CEILING(25) AS CeilValue; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_ceiling2)

### Example

Return the smallest integer value that is greater than or equal to a number:

```
SELECT CEILING(-13.5) AS CeilValue; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_ceiling3)
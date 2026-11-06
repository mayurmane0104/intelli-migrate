# SQL Server FLOOR() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_floor.asp](https://www.w3schools.com/sql/func_sqlserver_floor.asp)

---

# SQL Server FLOOR() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the largest integer value that is equal to or less than 25.75:

```
  SELECT FLOOR(25.75) AS FloorValue; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_floor)

## Definition and Usage

The FLOOR() function returns the largest integer value that is smaller than or equal to a number.

**Tip:** Also look at the [
CEILING()](func_sqlserver_ceiling.asp) and [ROUND()](func_sqlserver_round.asp) functions.

## Syntax

```
  FLOOR(
```
*number*)
## Parameter Values

| Parameter | Description | 
|---|---|
| number | Required. A numeric value | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

Ad

## More Examples

### Example

Return the largest integer value that is equal to or less than 25:

```
SELECT FLOOR(25) AS FloorValue; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_floor2)

### Example

Return the largest integer value that is equal to or less than -13.5:

```
SELECT FLOOR(-13.5) AS FloorValue; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_floor3)
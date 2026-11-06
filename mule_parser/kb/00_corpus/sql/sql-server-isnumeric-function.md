# SQL Server ISNUMERIC() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_isnumeric.asp](https://www.w3schools.com/sql/func_sqlserver_isnumeric.asp)

---

# SQL Server ISNUMERIC() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Tests whether the expression is numeric:

```
  SELECT ISNUMERIC(4567); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_isnumeric)

## Definition and Usage

The ISNUMERIC() function tests whether an expression is numeric.

This function returns 1 if the expression is numeric, otherwise it returns 0.

## Syntax

```
  ISNUMERIC(
```
*expression*)
## Parameter Values

| Parameter | Description | 
|---|---|
| expression | Required. The value to test | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

Ad

## More Examples

### Example

Tests whether the expression is numeric:

```
  SELECT ISNUMERIC('Hello world!'); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_isnumeric3)
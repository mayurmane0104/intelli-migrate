# SQL Server MAX() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_max.asp](https://www.w3schools.com/sql/func_sqlserver_max.asp)

---

# SQL Server MAX() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Find the price of the most expensive product in the "Products" table:

```
SELECT MAX(Price) AS LargestPrice FROM Products; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_max)

## Definition and Usage

The MAX() function returns the maximum value in a set of values.

**Note:** Also look at the [MIN()](func_sqlserver_min.asp) function.

## Syntax

```
  MAX(
```
*expression*)
## Parameter Values

| Parameter | Description | 
|---|---|
| expression | Required. A numeric value (can be a field or a formula) | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

Ad
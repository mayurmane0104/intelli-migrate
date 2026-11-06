# SQL Server MIN() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_min.asp](https://www.w3schools.com/sql/func_sqlserver_min.asp)

---

# SQL Server MIN() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Find the price of the cheapest product in the "Products" table:

```
SELECT MIN(Price) AS 
  SmallestPrice FROM Products; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_min)

## Definition and Usage

The MIN() function returns the minimum value in a set of values.

**Note:** Also look at the [MAX()](func_sqlserver_max.asp) function.

## Syntax

```
  MIN(
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
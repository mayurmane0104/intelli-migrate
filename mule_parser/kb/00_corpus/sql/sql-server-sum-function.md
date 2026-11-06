# SQL Server SUM() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_sum.asp](https://www.w3schools.com/sql/func_sqlserver_sum.asp)

---

# SQL Server SUM() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the sum of the "Quantity" field in the "OrderDetails" table:

```
  SELECT SUM(Quantity) AS TotalItemsOrdered FROM OrderDetails; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_sum)

## Definition and Usage

The SUM() function calculates the sum of a set of values.

**Note:** NULL values are ignored.

## Syntax

```
  SUM(
```
*expression*)
## Parameter Values

| Parameter | Description | 
|---|---|
| expression | Required. A field or a formula | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

Ad
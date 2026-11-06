# SQL Server COUNT() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_count.asp](https://www.w3schools.com/sql/func_sqlserver_count.asp)

---

# SQL Server COUNT() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the number of products in the "Products" table:

```
SELECT COUNT(ProductID) AS NumberOfProducts FROM Products; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_count)

## Definition and Usage

The COUNT() function returns the number of records returned by a select query.

**Note:** NULL values are not counted.

## Syntax

```
  COUNT
```
*(expression*)
## Parameter Values

| Parameter | Description | 
|---|---|
| expression | Required. A field or a string value | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

Ad
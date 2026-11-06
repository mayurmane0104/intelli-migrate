# SQL Server AVG() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_avg.asp](https://www.w3schools.com/sql/func_sqlserver_avg.asp)

---

# SQL Server AVG() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the average value for the "Price" column in the "Products" table:

```
SELECT AVG(Price) AS 
  AveragePrice FROM Products; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_avg)

## Definition and Usage

The AVG() function returns the average value of an expression.

**Note:** NULL values are ignored. 

## Syntax

```
  AVG(
```
*expression*)
## Parameter Values

| Parameter | Description | 
|---|---|
| expression | Required. A numeric value (can be a field or a formula) | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

## More Examples

### Example

Select all the products that have a price above the average price:

```
SELECT * FROM Products
WHERE Price > (SELECT AVG(Price) FROM Products);  
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_avg2)

Ad
# MS Access Avg() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_avg.asp](https://www.w3schools.com/sql/func_msaccess_avg.asp)

---

# MS Access Avg() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the average value for the "Price" column in the "Products" table:

```
SELECT Avg(Price) AS 
  AveragePrice FROM Products;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_avg&ss=-1)

## Definition and Usage

The Avg() function returns the average value of an expression.

**Note:** NULL values are ignored. 

## Syntax

```
  Avg(
```
*expression*)
## Parameter Values

| Parameter | Description | 
|---|---|
| expression | Required. A numeric value (can be a field or a formula) | 

## Technical Details

| Works in: | From Access 2000 | 
|---|

## More Examples

### Example

Select all the products that have a price above the average price:

```
SELECT * FROM Products
WHERE Price > (SELECT Avg(Price) FROM Products);  
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_avg_high&ss=-1)
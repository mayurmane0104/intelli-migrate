# MySQL AVG() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_avg.asp](https://www.w3schools.com/sql/func_mysql_avg.asp)

---

# MySQL AVG() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the average value for the "Price" column in the "Products" table:

```
SELECT AVG(Price) AS 
  AveragePrice FROM Products; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_avg)

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

| Works in: | From MySQL 4.0 | 
|---|

## More Examples

### Example

Select the records that have a price above the average price:

```
SELECT * FROM Products
WHERE Price > (SELECT AVG(Price) FROM Products);  
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_avg2)

Ad
# MySQL MIN() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_min.asp](https://www.w3schools.com/sql/func_mysql_min.asp)

---

# MySQL MIN() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Find the price of the cheapest product in the "Products" table:

```
SELECT MIN(Price) AS 
  SmallestPrice FROM Products; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_min)

## Definition and Usage

The MIN() function returns the minimum value in a set of values.

**Note:** See also the [MAX()](func_mysql_max.asp) function.

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

| Works in: | From MySQL 4.0 | 
|---|

Ad
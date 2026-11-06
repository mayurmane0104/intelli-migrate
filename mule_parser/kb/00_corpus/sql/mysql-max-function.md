# MySQL MAX() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_max.asp](https://www.w3schools.com/sql/func_mysql_max.asp)

---

# MySQL MAX() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Find the price of the most expensive product in the "Products" table:

```
SELECT MAX(Price) AS LargestPrice FROM Products; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_max)

## Definition and Usage

The MAX() function returns the maximum value in a set of values.

**Note:** See also the [MIN()](func_mysql_min.asp) function.

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

| Works in: | From MySQL 4.0 | 
|---|

Ad
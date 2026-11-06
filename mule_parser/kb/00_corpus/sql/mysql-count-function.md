# MySQL COUNT() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_count.asp](https://www.w3schools.com/sql/func_mysql_count.asp)

---

# MySQL COUNT() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the number of products in the "Products" table:

```
SELECT COUNT(ProductID) AS NumberOfProducts FROM Products; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_count)

## Definition and Usage

The COUNT() function returns the number of records returned by a select query.

**Note:** NULL values are not counted.

## Syntax

```
  COUNT(
```
*expression*)
## Parameter Values

| Parameter | Description | 
|---|---|
| expression | Required. A field or a string value | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

Ad
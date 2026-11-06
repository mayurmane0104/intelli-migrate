# MySQL SUM() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_sum.asp](https://www.w3schools.com/sql/func_mysql_sum.asp)

---

# MySQL SUM() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the sum of the "Quantity" field in the "OrderDetails" table:

```
  SELECT SUM(Quantity) AS TotalItemsOrdered FROM OrderDetails; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_sum)

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

| Works in: | From MySQL 4.0 | 
|---|

Ad
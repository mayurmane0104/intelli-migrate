# MS Access Sum() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_sum.asp](https://www.w3schools.com/sql/func_msaccess_sum.asp)

---

# MS Access Sum() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the sum of the "Quantity" field in the "OrderDetails" table:

```
  SELECT Sum(Quantity) AS TotalItemsOrdered FROM OrderDetails; 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_sum&ss=-1)

## Definition and Usage

The Sum() function calculates the sum of a set of values.

**Note:** NULL values are ignored.

## Syntax

```
  Sum(
```
*expression*)
## Parameter Values

| Parameter | Description | 
|---|---|
| expression | Required. A field or a formula | 

## Technical Details

| Works in: | From Access 2000 | 
|---|

Ad
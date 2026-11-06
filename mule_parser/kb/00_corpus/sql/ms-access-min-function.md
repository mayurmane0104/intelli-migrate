# MS Access Min() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_min.asp](https://www.w3schools.com/sql/func_msaccess_min.asp)

---

# MS Access Min() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Find the price of the cheapest product in the "Products" table:

```
SELECT 
  Min(Price) AS 
  SmallestPrice FROM Products;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_min&ss=-1)

## Definition and Usage

The Min() function returns the minimum value in a set of values.

**Note:** See also the [Max()](func_msaccess_max.asp) function.

## Syntax

```
  Min(
```
*expression*)
## Parameter Values

| Parameter | Description | 
|---|---|
| expression | Required. A numeric value (can be a field or a formula) | 

## Technical Details

| Works in: | From Access 2000 | 
|---|

Ad
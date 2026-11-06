# MS Access Max() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_max.asp](https://www.w3schools.com/sql/func_msaccess_max.asp)

---

# MS Access Max() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Find the price of the most expensive product in the "Products" table:

```
SELECT Max(Price) AS LargestPrice FROM Products;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_max&ss=-1)

## Definition and Usage

The Max() function returns the maximum value in a set of values.

**Note:** See also the [Min()](func_msaccess_min.asp) function.

## Syntax

```
  Max(
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
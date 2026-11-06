# MS Access Count() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_count.asp](https://www.w3schools.com/sql/func_msaccess_count.asp)

---

# MS Access Count() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the number of products in the "Products" table:

```
SELECT Count(ProductID) AS NumberOfProducts FROM Products; 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_count&ss=-1)

## Definition and Usage

The Count() function returns the number of records returned by a select query.

**Note:** NULL values are not counted. 

## Syntax

```
  Count(
```
*expression*)
## Parameter Values

| Parameter | Description | 
|---|---|
| expression | Required. A field or a string value | 

## Technical Details

| Works in: | From Access 2000 | 
|---|

Ad
# MS Access Int() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_int.asp](https://www.w3schools.com/sql/func_msaccess_int.asp)

---

# MS Access Int() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the integer part of a number:

```
SELECT Int(756.43) AS IntNum; 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_int&ss=-1)

## Definition and Usage

The Int() function returns the integer part of a number.

**Note:** If *number* is negative, this function returns 
the first negative integer less than or equal to *number*.

## Syntax

```
  Int(
```
*number*)
## Parameter Values

| Parameter | Description | 
|---|---|
| number | Required. A numeric value | 

## Technical Details

| Works in: | From Access 2000 | 
|---|

## More Examples

### Example

Return the integer part of the "Price" column:

```
  SELECT Int(Price) AS IntNum FROM Products;  
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_int2&ss=-1)

Ad
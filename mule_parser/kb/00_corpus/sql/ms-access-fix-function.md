# MS Access Fix() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_fix.asp](https://www.w3schools.com/sql/func_msaccess_fix.asp)

---

# MS Access Fix() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the integer part of a number:

```
SELECT Fix(756.43) AS FixNum; 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_fix&ss=-1)

## Definition and Usage

The Fix() function returns the integer part of a number.

## Syntax

```
  Fix(
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
  SELECT Fix(Price) AS FixNum FROM Products;  
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_fix2&ss=-1)

Ad
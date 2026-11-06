# MS Access IsNull() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_isnull.asp](https://www.w3schools.com/sql/func_msaccess_isnull.asp)

---

# MS Access IsNull() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Check whether the expression is a Null value:

```
SELECT IsNull(null); 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_isnull&ss=-1)

## Definition and Usage

The IsNull() function checks whether an expression contains Null (no data).

This function returns a Boolean value. TRUE (-1) indicates that the expression is a Null value, and FALSE (0) indicates that the expression is not a Null value.

## Syntax

```
  IsNull(
```
*expression*)
## Parameter Values

| Parameter | Description | 
|---|---|
| expression | Required. The value to test | 

## Technical Details

| Works in: | From Access 2000 | 
|---|

Ad

## More Examples

### Example

Return TRUE if the expression is a null value, otherwise FALSE:

```
SELECT IsNull("Hello"); 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_isnull2&ss=-1)

### Example

Return TRUE if the expression is a null value, otherwise FALSE:

```
SELECT IsNull(0); 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_isnull3&ss=-1)
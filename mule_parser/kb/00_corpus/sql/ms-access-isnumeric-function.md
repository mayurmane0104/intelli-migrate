# MS Access IsNumeric() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_isnumeric.asp](https://www.w3schools.com/sql/func_msaccess_isnumeric.asp)

---

# MS Access IsNumeric() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Check whether the expression is a valid number:

```
SELECT IsNumeric(1030); 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_isnumeric&ss=-1)

## Definition and Usage

The IsNumeric() function checks whether an expression is a valid number.

This function returns a Boolean value. TRUE (-1) indicates that the expression is a valid number, and FALSE (0) indicates that the expression is not a valid number.

## Syntax

```
  IsNumeric(
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

Return TRUE if the expression is a valid number, otherwise FALSE:

```
SELECT IsNumeric("Hello"); 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_isnumeric2&ss=-1)

### Example

Return TRUE if the expression is a valid number, otherwise FALSE:

```
SELECT IsNumeric("1030"); 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_isnumeric3&ss=-1)
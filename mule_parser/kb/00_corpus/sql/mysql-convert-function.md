# MySQL CONVERT() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_convert.asp](https://www.w3schools.com/sql/func_mysql_convert.asp)

---

# MySQL CONVERT() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Convert a value to a DATE datatype:

```
  SELECT 
  CONVERT("2017-08-29", DATE); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_convert)

## Definition and Usage

The CONVERT() function converts a value into the specified datatype or character set.

**Tip:** Also look at the [CAST()](func_mysql_cast.asp) function.

## Syntax

```
CONVERT(
```
*value*, *type*)
OR:

```
CONVERT(
```
*value* USING *charset*)
## Parameter Values

| Parameter | Description | ||||||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| value | Required. The value to convert | ||||||||||||||||||||
| type | Required. The datatype to convert to. Can be one of the following: 
 | ||||||||||||||||||||
| charset | Required. The character set to convert to | 

Ad

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

## More Examples

### Example

Convert a value to LATIN1 character set:

```
SELECT 
  CONVERT("W3Schools.com" USING latin1); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_convert4)
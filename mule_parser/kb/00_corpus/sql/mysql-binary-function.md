# MySQL BINARY Function

**Source:** [https://www.w3schools.com/sql/func_mysql_binary.asp](https://www.w3schools.com/sql/func_mysql_binary.asp)

---

# MySQL BINARY Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Convert a value to a binary string:

```
  SELECT BINARY "W3Schools.com"; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_binary)

## Definition and Usage

The BINARY function converts a value to a binary string.

This function is equivalent to using [CAST(value AS BINARY)](func_mysql_cast.asp).

## Syntax

```
  BINARY
```
* value*
## Parameter Values

| Parameter | Description | 
|---|---|
| value | Required. The value to convert | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

Ad

## More Examples

### Example

Here MySQL performs a character-by-character comparison of "HELLO" and "hello" and return 1 (because on a character-by-character basis, they are equivalent):

```
  SELECT "HELLO" = "hello"; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_binary2)

### Example

Here MySQL performs a byte-by-byte comparison of "HELLO" and "hello" and return 0 (because on a byte-by-byte basis, they are NOT equivalent):

```
  SELECT BINARY "HELLO" = "hello"; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_binary3)
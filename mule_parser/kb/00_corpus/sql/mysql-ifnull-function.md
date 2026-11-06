# MySQL IFNULL() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_ifnull.asp](https://www.w3schools.com/sql/func_mysql_ifnull.asp)

---

# MySQL IFNULL() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the specified value IF the expression is NULL, otherwise return the expression:

```
  SELECT IFNULL(NULL, "W3Schools.com"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_ifnull)

## Definition and Usage

The IFNULL() function returns a specified value if the expression is NULL.

If the expression is NOT NULL, this function returns the expression.

## Syntax

```
  IFNULL(
```
*expression*, *alt_value*)
## Parameter Values

| Parameter | Description | 
|---|---|
| expression | Required. The expression to test whether is NULL | 
| alt_value | Required. The value to return if expressionis NULL | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

Ad

## More Examples

### Example

Return the specified value IF the expression is NULL, otherwise return the expression:

```
  SELECT IFNULL("Hello", "W3Schools.com"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_ifnull2)

### Example

Return the specified value IF the expression is NULL, otherwise return the expression:

```
  SELECT IFNULL(NULL, 500); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_ifnull3)
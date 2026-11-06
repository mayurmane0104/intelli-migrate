# MySQL LEAST() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_least.asp](https://www.w3schools.com/sql/func_mysql_least.asp)

---

# MySQL LEAST() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the smallest value of the list of arguments:

```
  SELECT LEAST(3, 12, 34, 8, 25); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_least)

## Definition and Usage

The LEAST() function returns the smallest value of the list of arguments.

**Note:** See also the [
GREATEST()](func_mysql_greatest.asp) function.

## Syntax

```
  LEAST(
```
*arg1*, *arg2*, *arg3*, ...)
## Parameter Values

| Parameter | Description | 
|---|---|
| arg1,arg2,arg3, ... | Required. The list of arguments to be evaluated | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

## More Examples

### Example

Return the smallest value of the list of arguments:

```
  SELECT LEAST("w3Schools.com", "microsoft.com", "apple.com"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_least2)

Ad
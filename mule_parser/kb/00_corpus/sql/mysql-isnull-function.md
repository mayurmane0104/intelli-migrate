# MySQL ISNULL() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_isnull.asp](https://www.w3schools.com/sql/func_mysql_isnull.asp)

---

# MySQL ISNULL() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Test whether an expression is NULL:

```
  SELECT ISNULL(NULL); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_isnull)

## Definition and Usage

The ISNULL() function returns 1 or 0 depending on whether an expression is NULL.

If expression is NULL, this function returns 1. Otherwise, it returns 0.

## Syntax

```
  ISNULL(
```
*expression*)
## Parameter Values

| Parameter | Description | 
|---|---|
| expression | Required. The value to test | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

Ad
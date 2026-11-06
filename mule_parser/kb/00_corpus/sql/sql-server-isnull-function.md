# SQL Server ISNULL() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_isnull.asp](https://www.w3schools.com/sql/func_sqlserver_isnull.asp)

---

# SQL Server ISNULL() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the specified value IF the expression is NULL, otherwise return the expression:

```
  SELECT ISNULL(NULL, 'W3Schools.com'); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_isnull)

## Definition and Usage

The ISNULL() function returns a specified value if the expression is NULL.

If the expression is NOT NULL, this function returns the expression.

## Syntax

```
  ISNULL(
```
*expression*, *value*)
## Parameter Values

| Parameter | Description | 
|---|---|
| expression | Required. The expression to test whether is NULL | 
| value | Required. The value to return if expressionis NULL | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

Ad

## More Examples

### Example

Return the specified value IF the expression is NULL, otherwise return the expression:

```
  SELECT ISNULL('Hello', 'W3Schools.com'); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_isnull2)

### Example

Return the specified value IF the expression is NULL, otherwise return the expression:

```
  SELECT ISNULL(NULL, 500); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_isnull3)
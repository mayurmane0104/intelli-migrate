# SQL Server DATALENGTH() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_datalength.asp](https://www.w3schools.com/sql/func_sqlserver_datalength.asp)

---

# SQL Server DATALENGTH() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the length of an expression (in bytes):

```
  SELECT 
  DATALENGTH('W3Schools.com'); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_datalength)

## Definition and Usage

The DATALENGTH() function returns the number of bytes used to represent an expression.

**Note:** The DATALENGTH() function counts both leading and 
trailing spaces when calculating the length of the expression.

**Tip:** Also see the [LEN()](func_sqlserver_len.asp) function.

## Syntax

```
  DATALENGTH(
```
*expression*)
## Parameter Values

| Parameter | Description | 
|---|---|
| expression | Required. The data type to return the length for. If 
    expressionis NULL, it returns NULL | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

Ad

## More Examples

### Example

Return the length of an expression (in bytes) (counts both leading and trailing spaces):

```
  SELECT 
  DATALENGTH('   W3Schools.com   '); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_datalength2)

### Example

Return the length of an expression (in bytes):

```
  SELECT 
  DATALENGTH('2017-08'); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_datalength3)
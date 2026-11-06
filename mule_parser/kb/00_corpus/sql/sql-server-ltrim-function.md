# SQL Server LTRIM() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_ltrim.asp](https://www.w3schools.com/sql/func_sqlserver_ltrim.asp)

---

# SQL Server LTRIM() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Remove leading spaces from a string:

```
  SELECT LTRIM('     SQL Tutorial') AS LeftTrimmedString; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_ltrim)

## Definition and Usage

The LTRIM() function removes leading spaces from a string.

**Note:** Also look at the [RTRIM()](func_sqlserver_rtrim.asp) function.

## Syntax

```
  LTRIM(
```
*string*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string | Required. The string to remove leading spaces from | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

Ad
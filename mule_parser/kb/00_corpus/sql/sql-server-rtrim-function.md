# SQL Server RTRIM() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_rtrim.asp](https://www.w3schools.com/sql/func_sqlserver_rtrim.asp)

---

# SQL Server RTRIM() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Remove trailing spaces from a string:

```
  SELECT RTRIM('SQL Tutorial     ') AS RightTrimmedString; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_rtrim)

## Definition and Usage

The RTRIM() function removes trailing spaces from a string.

**Note:** Also look at the [LTRIM()](func_sqlserver_ltrim.asp) function.

## Syntax

```
  RTRIM(
```
*string*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string | Required. The string to remove trailing spaces from | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

Ad
# SQL Server SYSDATETIME() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_sysdatetime.asp](https://www.w3schools.com/sql/func_sqlserver_sysdatetime.asp)

---

# SQL Server SYSDATETIME() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the date and time of the SQL Server:

```
  SELECT SYSDATETIME() AS SysDateTime; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_sysdatetime)

## Definition and Usage

The SYSDATETIME() function returns the date and time of the computer where the SQL Server is running.

## Syntax

```
  SYSDATETIME()
```
## Technical Details

| Return type: | datetime2(7) | 
|---|---|
| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 

Ad
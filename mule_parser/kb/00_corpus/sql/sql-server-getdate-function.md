# SQL Server GETDATE() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_getdate.asp](https://www.w3schools.com/sql/func_sqlserver_getdate.asp)

---

# SQL Server GETDATE() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the current database system date and time:

```
  SELECT 
  GETDATE(); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_getdate)

## Definition and Usage

The GETDATE() function returns the current database system date and time, in a 'YYYY-MM-DD hh:mm:ss.mmm' format.

**Tip:** Also look at the
[CURRENT_TIMESTAMP](func_sqlserver_current_timestamp.asp) function.

## Syntax

```
  GETDATE()
```
## Technical Details

| Return type: | datetime | 
|---|---|
| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 

Ad
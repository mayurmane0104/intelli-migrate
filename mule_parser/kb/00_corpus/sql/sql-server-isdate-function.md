# SQL Server ISDATE() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_isdate.asp](https://www.w3schools.com/sql/func_sqlserver_isdate.asp)

---

# SQL Server ISDATE() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Check if the expression is a valid date:

```
  SELECT ISDATE('2017-08-25'); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_isdate)

## Definition and Usage

The ISDATE() function checks an expression and returns 1 if it is a valid date, otherwise 0.

## Syntax

```
  ISDATE(
```
*expression*)
## Parameter Values

| Parameter | Description | 
|---|---|
| expression | Required. The expression to test | 

## Technical Details

| Return type: | int | 
|---|---|
| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 

Ad
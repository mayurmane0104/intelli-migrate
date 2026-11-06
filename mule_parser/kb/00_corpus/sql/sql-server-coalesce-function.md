# SQL Server COALESCE() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_coalesce.asp](https://www.w3schools.com/sql/func_sqlserver_coalesce.asp)

---

# SQL Server COALESCE() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the first non-null value in a list:

```
  SELECT 
  COALESCE(NULL, NULL, NULL, 'W3Schools.com', NULL, 'Example.com'); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_coalesce)

## Definition and Usage

The COALESCE() function returns the first non-null value in a list.

## Syntax

```
  COALESCE(
```
*val1*, *
  val2*, *....*, *val_n*)
## Parameter Values

| Parameter | Description | 
|---|---|
| val1, val2, val_n | Required. The values to test | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

## More Examples

### Example

Return the first non-null value in a list:

```
  SELECT 
  COALESCE(NULL, 1, 2, 'W3Schools.com'); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_coalesce2)

Ad
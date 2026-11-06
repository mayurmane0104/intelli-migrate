# SQL Server REPLICATE() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_replicate.asp](https://www.w3schools.com/sql/func_sqlserver_replicate.asp)

---

# SQL Server REPLICATE() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Repeat a string:

```
  SELECT REPLICATE('SQL Tutorial', 5); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_replicate)

## Definition and Usage

The REPLICATE() function repeats a string a specified number of times.

## Syntax

```
REPLICATE(
```
*string, integer*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string | Required. The string to repeat | 
| integer | Required. The number of times to repeat the string | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

## More Examples

### Example

Repeat the text in CustomerName two times:

```
  SELECT REPLICATE(CustomerName, 2)
FROM Customers; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_replicate2)

Ad
# SQL Server LOWER() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_lower.asp](https://www.w3schools.com/sql/func_sqlserver_lower.asp)

---

# SQL Server LOWER() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Convert the text to lower-case:

```
SELECT LOWER('SQL Tutorial is FUN!'); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_lower)

## Definition and Usage

The LOWER() function converts a string to lower-case.

**Note:** Also look at the [ UPPER()](func_sqlserver_upper.asp) function.

## Syntax

```
  LOWER(
```
*text*)
## Parameter Values

| Parameter | Description | 
|---|---|
| text | Required. The string to convert | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

## More Examples

### Example

Convert the text in "CustomerName" to lower-case:

```
SELECT LOWER(CustomerName) AS LowercaseCustomerName
FROM Customers; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_lower2)

Ad
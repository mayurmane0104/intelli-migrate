# SQL Server UPPER() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_upper.asp](https://www.w3schools.com/sql/func_sqlserver_upper.asp)

---

# SQL Server UPPER() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Convert the text to upper-case:

```
SELECT UPPER('SQL Tutorial is FUN!'); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_upper)

## Definition and Usage

The UPPER() function converts a string to upper-case.

**Note:** Also look at the [LOWER()](func_sqlserver_lower.asp) function.

## Syntax

```
  UPPER(
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

Convert the text in "CustomerName" to upper-case:

```
SELECT UPPER(CustomerName) AS UppercaseCustomerName
FROM Customers; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_upper2)

Ad
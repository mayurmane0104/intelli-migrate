# SQL Server UNICODE() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_unicode.asp](https://www.w3schools.com/sql/func_sqlserver_unicode.asp)

---

# SQL Server UNICODE() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return an integer value (the Unicode value), for the first character of the input expression:

```
  SELECT UNICODE('Atlanta'); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_unicode)

## Definition and Usage

The UNICODE() function returns an integer value (the Unicode value), for the first character of the input expression.

## Syntax

```
  UNICODE(
```
*character_expression*)
## Parameter Values

| Parameter | Description | 
|---|---|
| character_expression | Required. An nchar or varchar expression | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

## More Examples

### Example

Return an integer value (the Unicode value), for the first character of the input expression:

```
  SELECT UNICODE(CustomerName) AS UnicodeOfFirstChar
FROM Customers; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_unicode2)

Ad
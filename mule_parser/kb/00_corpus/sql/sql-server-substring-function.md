# SQL Server SUBSTRING() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_substring.asp](https://www.w3schools.com/sql/func_sqlserver_substring.asp)

---

# SQL Server SUBSTRING() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Extract 3 characters from a string, starting in position 1:

```
  SELECT SUBSTRING('SQL Tutorial', 1, 3) AS ExtractString; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_substring)

## Definition and Usage

The SUBSTRING() function extracts some characters from a string.

## Syntax

```
  SUBSTRING(
```
*string*, *start*, *length*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string | Required. The string to extract from | 
| start | Required. The start position. The first position in stringis 1 | 
| length | Required. The number of characters to extract. Must be a positive number | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

Ad

## More Examples

### Example

Extract 5 characters from the "CustomerName" column, starting in position 1:

```
  SELECT SUBSTRING(CustomerName, 1, 5) AS ExtractString
FROM Customers; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_substring2)

### Example

Extract 100 characters from a string, starting in position 1:

```
  SELECT SUBSTRING('SQL Tutorial', 1, 100) AS ExtractString; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_substring3)
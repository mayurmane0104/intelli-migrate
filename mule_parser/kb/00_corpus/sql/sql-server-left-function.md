# SQL Server LEFT() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_left.asp](https://www.w3schools.com/sql/func_sqlserver_left.asp)

---

# SQL Server LEFT() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Extract 3 characters from a string (starting from left):

```
  SELECT LEFT('SQL Tutorial', 3) AS ExtractString; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_left)

## Definition and Usage

The LEFT() function extracts a number of characters from a string (starting from left).

## Syntax

```
  LEFT(
```
*string*, *number_of_chars*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string | Required. The string to extract from | 
| number_of_chars | Required. The number of characters to extract. If the number exceeds the number of characters in string, 
    it returnsstring | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

Ad

## More Examples

### Example

Extract 5 characters from the text in the "CustomerName" column (starting from left):

```
  SELECT LEFT(CustomerName, 5) AS ExtractString
FROM Customers; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_left2)

### Example

Extract 100 characters from a string (starting from left):

```
  SELECT LEFT('SQL Tutorial', 100) AS ExtractString; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_left3)
# SQL Server RIGHT() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_right.asp](https://www.w3schools.com/sql/func_sqlserver_right.asp)

---

# SQL Server RIGHT() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Extract 3 characters from a string (starting from right):

```
  SELECT RIGHT('SQL Tutorial', 3) AS ExtractString; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_right)

## Definition and Usage

The RIGHT() function extracts a number of characters from a string (starting from right).

## Syntax

```
  RIGHT(
```
*string*, *number_of_chars*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string | Required. The string to extract from | 
| number_of_chars | Required. The number of characters to extract. If number_of_chars>string, 
    it returnsstring | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

Ad

## More Examples

### Example

Extract 5 characters from the text in the "CustomerName" column (starting from right):

```
  SELECT RIGHT(CustomerName, 5) AS ExtractString
FROM Customers; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_right2)

### Example

Extract 100 characters from a string (starting from right):

```
  SELECT RIGHT('SQL Tutorial', 100) AS ExtractString; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_right3)
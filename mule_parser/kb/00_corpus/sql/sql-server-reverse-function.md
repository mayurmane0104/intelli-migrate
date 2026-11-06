# SQL Server REVERSE() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_reverse.asp](https://www.w3schools.com/sql/func_sqlserver_reverse.asp)

---

# SQL Server REVERSE() Function

## Definition and Usage

The REVERSE() function reverses a string and returns the result.

## Syntax

```
REVERSE(
```
*string*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string | Required. The string to reverse | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

## More Examples

### Example

Reverse the text in CustomerName:

```
  SELECT REVERSE(CustomerName)
FROM Customers; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_reverse2)

Ad
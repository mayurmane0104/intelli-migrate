# SQL Server IIF() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_iif.asp](https://www.w3schools.com/sql/func_sqlserver_iif.asp)

---

# SQL Server IIF() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return "YES" if the condition is TRUE, or "NO" if the condition is FALSE:

```
  SELECT 
  IIF(500<1000, 'YES', 'NO'); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_iif)

## Definition and Usage

The IIF() function returns a value if a condition is TRUE, or another value if a condition is FALSE.

## Syntax

```
  IIF(
```
*condition*, *value_if_true*, *value_if_false*)
## Parameter Values

| Parameter | Description | 
|---|---|
| condition | Required. The value to test | 
| value_if_true | Optional. The value to return if conditionis TRUE | 
| value_if_false | Optional. The value to return if conditionis FALSE | 

## Technical Details

| Works in: | SQL Server (starting with 2012), Azure SQL Database | 
|---|

Ad

## More Examples

### Example

Return 5 if the condition is TRUE, or 10 if the condition is FALSE:

```
  SELECT IIF(500<1000, 5, 10); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_iif2)

### Example

Test whether two strings are the same and return "YES" if they are, or "NO" if not:

```
  SELECT IIF('hello' = 'bye', 'YES', 'NO'); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_iif3)

### Example

Return "MORE" if the condition is TRUE, or "LESS" if the condition is FALSE:

```
  SELECT OrderID, Quantity, IIF(Quantity>10, 
  'MORE', 'LESS')
FROM 
  OrderDetails; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_iif4)
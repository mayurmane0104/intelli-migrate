# SQL Server CONCAT() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_concat.asp](https://www.w3schools.com/sql/func_sqlserver_concat.asp)

---

# SQL Server CONCAT() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Add two strings together:

```
  SELECT 
  CONCAT('W3Schools', '.com'); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_concat)

## Definition and Usage

The CONCAT() function adds two or more strings together.

**Note:** See also [
Concat with the + operator](func_sqlserver_concat_with_plus.asp) and [
CONCAT_WS()](func_sqlserver_concat_ws.asp).

## Syntax

```
  CONCAT(
```
*string1*, *
  string2*, *....*, *string_n*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string1, string2, string_n | Required. The strings to add together | 

## Technical Details

| Works in: | SQL Server (starting with 2012), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

Ad

## More Examples

### Example

Add strings together (separate each string with a space character):

```
  SELECT 
  CONCAT('SQL', ' ', 'is', ' ', 'fun!'); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_concat3)
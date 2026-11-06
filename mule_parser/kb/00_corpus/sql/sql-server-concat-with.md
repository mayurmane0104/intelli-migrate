# SQL Server Concat with +

**Source:** [https://www.w3schools.com/sql/func_sqlserver_concat_with_plus.asp](https://www.w3schools.com/sql/func_sqlserver_concat_with_plus.asp)

---

# SQL Server Concat With +

### Example[Get your own SQL Server](/sql/sql_server.asp)

Add 2 strings together:

```
  SELECT 
  'W3Schools' + '.com'; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_concat_plus)

## Definition and Usage

The + operator allows you to add two or more strings together.

**Note:** See also the [
CONCAT()](func_sqlserver_concat.asp) and [CONCAT_WS()](func_sqlserver_concat_ws.asp) functions.

## Syntax

```
  
```
*string1 +
  string2 + string_n*
## Parameter Values

| Parameter | Description | 
|---|---|
| string1, string2, string_n | Required. The strings to add together | 

## Technical Details

| Works in: | SQL Server (starting with 2005), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

## More Examples

### Example

Add strings together (separate each string with a space character):

```
  SELECT 
  'SQL' + ' ' + 'is' + ' ' + 'fun!'; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_concat_plus3)
# SQL Server CONCAT_WS() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_concat_ws.asp](https://www.w3schools.com/sql/func_sqlserver_concat_ws.asp)

---

# SQL Server CONCAT_WS() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Add strings together. Use '.' to separate the concatenated string values:

```
  SELECT 
  CONCAT_WS('.', 'www', 'W3Schools', 'com'); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_concat_ws)

## Definition and Usage

The CONCAT_WS() function adds two or more strings together with a separator.

**Note:** See also [CONCAT()](func_sqlserver_concat.asp) and
[
Concat with the + operator](func_sqlserver_concat_with_plus.asp).

## Syntax

```
  CONCAT_WS(
```
*separator, string1*, *
  string2*, *....*, *string_n*)
## Parameter Values

| Parameter | Description | 
|---|---|
| separator | Required. The separator to use | 
| string1, string2, string_n | Required. The strings to add together | 

## Technical Details

| Works in: | SQL Server (starting with 2017), Azure SQL Database, Azure SQL Data Warehouse | 
|---|

## More Examples

### Example

Add strings together. Use '-' to separate the concatenated string values:

```
  SELECT 
  CONCAT_WS('-', 'SQL', ' is', ' fun!'); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_concat_ws2)
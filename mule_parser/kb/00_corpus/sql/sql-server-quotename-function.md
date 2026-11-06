# SQL Server QUOTENAME() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_quotename.asp](https://www.w3schools.com/sql/func_sqlserver_quotename.asp)

---

# SQL Server QUOTENAME() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return a Unicode string with bracket delimiters (default):

```
  SELECT QUOTENAME('abcdef'); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_quotename)

## Definition and Usage

The QUOTENAME() function returns a Unicode string with delimiters added to make the string a valid SQL Server delimited identifier.

## Syntax

```
  QUOTENAME(
```
*string, quote_char*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string | Required. A string of Unicode character data. Limited to 128 characters | 
| quote_char | Optional. A one-character string to use as the delimiter. Can be a 
    single quotation mark ( ' ), a left or right bracket ( [] ), a double 
    quotation mark ( " ), a left or right parenthesis ( () ), a greater than or 
    less than sign ( >< ), a left or right brace ( {} ) or a backtick ( ` ). If quote_charis not specified, brackets are used. | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

## More Examples

### Example

Return a Unicode string with parenthesis delimiters:

```
  SELECT QUOTENAME('abcdef', '()'); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_quotename2)

Ad
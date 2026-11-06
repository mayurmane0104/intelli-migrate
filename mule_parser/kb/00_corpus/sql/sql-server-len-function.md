# SQL Server LEN() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_len.asp](https://www.w3schools.com/sql/func_sqlserver_len.asp)

---

# SQL Server LEN() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the length of a string:

```
  SELECT 
  LEN('W3Schools.com'); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_len)

## Definition and Usage

The LEN() function returns the length of a string.

**Note:** Trailing spaces at 
the end of the string is not included when calculating the length. However, leading spaces at the start of the string 
is included when calculating the length.

**Tip:** Also look at the [DATALENGTH()](func_sqlserver_datalength.asp) function.

## Syntax

```
  LEN(
```
*string*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string | Required. The string to return the length for. If stringis NULL, it returns NULL | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

## More Examples

### Example

Return the length of a string (counts leading spaces, but not trailing spaces):

```
  SELECT 
  LEN(' W3Schools.com '); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_len2)
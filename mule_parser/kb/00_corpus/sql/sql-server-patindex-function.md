# SQL Server PATINDEX() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_patindex.asp](https://www.w3schools.com/sql/func_sqlserver_patindex.asp)

---

# SQL Server PATINDEX() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the position of a pattern in a string:

```
  SELECT PATINDEX('%schools%', 'W3Schools.com'); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_patindex)

## Definition and Usage

The PATINDEX() function returns the position of a pattern in a string.

If the pattern is not found, this function returns 0.

**Note:** The search is case-insensitive and the first position in *string* is 1.

## Syntax

```
  PATINDEX(%
```
*pattern*%, *string*)
## Parameter Values

| Parameter | Description | 
|---|---|
| % pattern% | Required. The pattern to find. It MUST be surrounded by %. Other wildcards 
    can be used in pattern, such as:
 | 
| string | Required. The string to be searched | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

Ad

## More Examples

### Example

Return the position of a pattern in a string:

```
  SELECT 
  PATINDEX('%s%com%', 'W3Schools.com'); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_patindex2)

### Example

Return the position of a pattern in a string:

```
  SELECT PATINDEX('%[ol]%', 'W3Schools.com'); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_patindex3)

### Example

Return the position of a pattern in a string:

```
  SELECT PATINDEX('%[z]%', 'W3Schools.com'); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_patindex4)
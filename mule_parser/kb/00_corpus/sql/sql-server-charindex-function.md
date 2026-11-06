# SQL Server CHARINDEX() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_charindex.asp](https://www.w3schools.com/sql/func_sqlserver_charindex.asp)

---

# SQL Server CHARINDEX() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Search for "t" in string "Customer", and return position:

```
  SELECT 
  CHARINDEX('t', 'Customer') AS MatchPosition; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_charindex)

## Definition and Usage

The CHARINDEX() function searches for a substring in a string, and returns the position.

If the substring is not found, this function returns 0.

**Note:** This function performs a case-insensitive search.

## Syntax

```
  CHARINDEX(
```
*substring*, *
  string*, *start*)
## Parameter Values

| Parameter | Description | 
|---|---|
| substring | Required. The substring to search for | 
| string | Required. The string to be searched | 
| start | Optional. The position where the search will start (if you do not want 
    to start at the beginning of s tring). 
    The first position instringis 1 | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

Ad

## More Examples

### Example

Search for "OM" in string "Customer", and return position:

```
  SELECT 
  CHARINDEX('OM', 'Customer') AS MatchPosition;  
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_charindex2)

### Example

Search for "mer" in string "Customer", and return position (start in position 3):

```
  SELECT CHARINDEX('mer', 'Customer', 3) AS MatchPosition;  
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_charindex3)
# SQL Server REPLACE() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_replace.asp](https://www.w3schools.com/sql/func_sqlserver_replace.asp)

---

# SQL Server REPLACE() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Replace "T" with "M":

```
  SELECT REPLACE('SQL Tutorial', 'T', 'M'); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_replace)

## Definition and Usage

The REPLACE() function replaces all occurrences of a substring within a string, with a new substring.

**Note:** The search is case-insensitive.

**Tip:** Also look at the [STUFF()](func_sqlserver_stuff.asp) function.

## Syntax

```
  REPLACE(
```
*string*, *old_string*, *new_string*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string | Required. The original string | 
| old_string | Required. The string to be replaced | 
| new_string | Required. The new replacement string | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|